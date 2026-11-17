import pandas as pd
df = pd.read_excel("MENTBR25.xlsx", dtype=str)
df[df["ID_MN_RESI"] == "291650"]