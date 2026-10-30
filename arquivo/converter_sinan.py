#!/usr/bin/env python3

import sys
import struct
from pathlib import Path

import pandas as pd


# ============================================================
# DBC -> DBF
# Formato utilizado pelo DATASUS
# ============================================================

MAXBITS = 13

litlen = [
    11,124,8,7,28,7,188,13,76,4,10,8,12,10,12,10,8,23,8,
    9,7,6,7,8,7,6,55,8,23,24,12,11,7,9,11,12,6,7,22,5,
    7,24,6,11,9,6,7,22,7,11,38,7,9,8,25,11,8,11,9,12,
    8,12,5,38,5,38,5,11,7,5,6,21,6,10,53,8,7,24,10,27,
    44,253,253,253,252,252,252,13,12,45,12,45,12,61,12,45,
    44,173
]

lenlen = [2,35,36,53,38,23]

distlen = [2,20,53,230,247,151,248]


base = [
    3,2,4,5,6,7,8,9,
    10,12,16,24,40,72,136,264
]

extra = [
    0,0,0,0,0,0,0,0,
    1,2,3,4,5,6,7,8
]


def construct_table(rep):

    lengths = []

    for x in rep:
        lengths.extend(
            [x & 15] * ((x >> 4) + 1)
        )

    counts = [0] * (MAXBITS + 1)

    for length in lengths:
        counts[length] += 1

    symbols = []

    for length in range(1, MAXBITS + 1):
        symbols.extend(
            i for i, value in enumerate(lengths)
            if value == length
        )

    return counts, symbols


litcnt, litsym = construct_table(litlen)
lencnt, lensym = construct_table(lenlen)
distcnt, distsym = construct_table(distlen)


class BitReader:

    def __init__(self, data):

        self.data = data
        self.position = 0
        self.buffer = 0
        self.bits_available = 0


    def bits(self, amount):

        value = self.buffer

        while self.bits_available < amount:

            if self.position >= len(self.data):
                raise EOFError(
                    "Fim inesperado do arquivo DBC."
                )

            value |= (
                self.data[self.position]
                << self.bits_available
            )

            self.position += 1
            self.bits_available += 8

        result = value & ((1 << amount) - 1)

        self.buffer = value >> amount
        self.bits_available -= amount

        return result


def decode(reader, counts, symbols):

    code = 0
    first = 0
    index = 0

    for length in range(1, MAXBITS + 1):

        bit = reader.bits(1)

        code = (code << 1) | (bit ^ 1)

        count = counts[length]

        if code < first + count:

            return symbols[
                index + code - first
            ]

        index += count

        first = (first + count) << 1

    raise ValueError(
        "Código Huffman inválido."
    )


def decompress_dbc(data):

    reader = BitReader(data)

    literal_mode = reader.bits(8)
    dictionary_bits = reader.bits(8)

    if literal_mode not in (0, 1):

        raise ValueError(
            "Arquivo DBC inválido."
        )

    if dictionary_bits not in (4, 5, 6):

        raise ValueError(
            "Tamanho de dicionário inválido."
        )

    output = bytearray()

    while True:

        if reader.bits(1):

            symbol = decode(
                reader,
                lencnt,
                lensym
            )

            length = (
                base[symbol]
                + reader.bits(extra[symbol])
            )

            if length == 519:
                break

            dbits = (
                2
                if length == 2
                else dictionary_bits
            )

            distance = (
                decode(
                    reader,
                    distcnt,
                    distsym
                )
                << dbits
            )

            distance += reader.bits(dbits) + 1

            if distance > len(output):

                raise ValueError(
                    "Distância inválida durante a descompressão."
                )

            for _ in range(length):

                output.append(
                    output[-distance]
                )

        else:

            if literal_mode:

                value = decode(
                    reader,
                    litcnt,
                    litsym
                )

            else:

                value = reader.bits(8)

            output.append(value)

    return bytes(output)


def dbc_to_dbf(input_file, output_file):

    print(f"\nConvertendo:")
    print(f"  {input_file}")

    data = Path(input_file).read_bytes()

    # Tamanho do cabeçalho DBF
    header_size = struct.unpack_from(
        "<H",
        data,
        8
    )[0]

    # Após o cabeçalho existe um CRC de 4 bytes
    compressed_data = data[
        header_size + 4:
    ]

    decompressed = decompress_dbc(
        compressed_data
    )

    dbf = (
        data[:header_size]
        + decompressed
    )

    Path(output_file).write_bytes(dbf)

    print(f"DBF criado:")
    print(f"  {output_file}")

    return output_file


# ============================================================
# DBF -> DataFrame
# ============================================================

def dbf_to_dataframe(dbf_file):

    data = Path(dbf_file).read_bytes()

    number_records = struct.unpack_from(
        "<I",
        data,
        4
    )[0]

    header_size = struct.unpack_from(
        "<H",
        data,
        8
    )[0]

    record_size = struct.unpack_from(
        "<H",
        data,
        10
    )[0]

    fields = []

    position = 32

    while data[position] != 0x0D:

        field = data[
            position:
            position + 32
        ]

        name = (
            field[:11]
            .split(b"\0", 1)[0]
            .decode(
                "latin1"
            )
        )

        field_type = chr(field[11])

        field_length = field[16]

        decimals = field[17]

        fields.append(
            (
                name,
                field_type,
                field_length,
                decimals
            )
        )

        position += 32

    rows = []

    for record_number in range(number_records):

        start = (
            header_size
            + record_number * record_size
        )

        end = start + record_size

        record = data[start:end]

        offset = 1

        values = []

        for (
            name,
            field_type,
            field_length,
            decimals
        ) in fields:

            raw = record[
                offset:
                offset + field_length
            ]

            offset += field_length

            if field_type == "D":

                value = (
                    raw
                    .decode("ascii", errors="ignore")
                    .strip()
                )

            elif field_type == "N":

                value = (
                    raw
                    .decode("ascii", errors="ignore")
                    .strip()
                )

                if value:

                    if decimals == 0:

                        value = int(value)

                    else:

                        value = float(value)

                else:

                    value = None

            else:

                value = (
                    raw
                    .decode(
                        "cp1252",
                        errors="replace"
                    )
                    .strip()
                )

            values.append(value)

        rows.append(values)

    columns = [
        field[0]
        for field in fields
    ]

    return pd.DataFrame(
        rows,
        columns=columns
    )


# ============================================================
# Programa principal
# ============================================================

def main():

    if len(sys.argv) < 2:

        print(
            "\nUso:"
        )

        print(
            "  python converter_sinan.py arquivo.dbc"
        )

        print(
            "\nExemplo:"
        )

        print(
            "  python converter_sinan.py MENTBR13.dbc"
        )

        sys.exit(1)


    input_file = Path(sys.argv[1])

    if not input_file.exists():

        print(
            f"Erro: arquivo não encontrado: {input_file}"
        )

        sys.exit(1)


    if input_file.suffix.lower() != ".dbc":

        print(
            "Erro: o arquivo precisa ter extensão .dbc"
        )

        sys.exit(1)


    # --------------------------------------------------------
    # DBC -> DBF
    # --------------------------------------------------------

    dbf_file = input_file.with_suffix(".dbf")

    dbc_to_dbf(
        input_file,
        dbf_file
    )


    # --------------------------------------------------------
    # DBF -> DataFrame
    # --------------------------------------------------------

    print(
        "\nLendo banco de dados..."
    )

    df = dbf_to_dataframe(
        dbf_file
    )


    print(
        f"Registros encontrados: {len(df)}"
    )

    print(
        f"Campos encontrados: {len(df.columns)}"
    )


    # --------------------------------------------------------
    # DBF -> CSV
    # --------------------------------------------------------

    csv_file = input_file.with_suffix(
        ".csv"
    )

    df.to_csv(
        csv_file,
        index=False,
        sep=";",
        encoding="utf-8-sig"
    )


    print(
        f"\nCSV criado:"
    )

    print(
        f"  {csv_file}"
    )


    # --------------------------------------------------------
    # Filtrar Burnout Z73.0
    # --------------------------------------------------------

    # Procuramos automaticamente por campos que
    # possam conter o CID.
    possible_cid_fields = [
        column
        for column in df.columns
        if (
            "CID" in column.upper()
            or "DIAG" in column.upper()
        )
    ]


    if possible_cid_fields:

        print(
            "\nCampos relacionados ao diagnóstico:"
        )

        for field in possible_cid_fields:

            print(
                f"  - {field}"
            )


        # Usamos DIAG_ESP se existir.
        if "DIAG_ESP" in df.columns:

            cid_column = "DIAG_ESP"

            cid = (
                df[cid_column]
                .astype(str)
                .str.upper()
                .str.replace(
                    ".",
                    "",
                    regex=False
                )
                .str.strip()
            )

            burnout = df[
                cid == "Z730"
            ].copy()


            burnout_file = (
                input_file.parent
                / f"{input_file.stem}_BURNOUT_Z730.csv"
            )


            burnout.to_csv(
                burnout_file,
                index=False,
                sep=";",
                encoding="utf-8-sig"
            )


            print(
                "\n================================"
            )

            print(
                "BURNOUT / CID-10 Z73.0"
            )

            print(
                "================================"
            )

            print(
                f"Casos encontrados: {len(burnout)}"
            )

            print(
                f"Arquivo:"
            )

            print(
                f"  {burnout_file}"
            )


            # Também gera Excel
            excel_file = (
                input_file.parent
                / f"{input_file.stem}_BURNOUT_Z730.xlsx"
            )


            burnout.to_excel(
                excel_file,
                index=False
            )


            print(
                f"\nExcel:"
            )

            print(
                f"  {excel_file}"
            )


    print(
        "\nConversão concluída!"
    )


if __name__ == "__main__":

    main()
