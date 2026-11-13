# Projeto Extensionista

## Principal

- formular pergunta respondível com dados
- indicar público - Trabalhadores
- território - São Paulo, Minas Gerais, DF (taxa alta), (Estado com menor taxa)
- período - 5 anos - 2020 até 2025
- fonte oficial - DATASUS
- ODS - 3 – Saúde e Bem-Estar.
- contrato de equipe (diário de bordo)

## Objetivo

- Qual a taxa de mudança de burnout entre algum ano até outro ano nos Estados?
- Por que esses Estados escolhidos? R: Correlação de dados. Proporção populacional não interfere na taxa.
- Pandemia vs burnout

Comparar a taxa de burnout entre o de Estado de São Paulo e o Estado de Minas Gerias.

- Coletar os dados
- Cálculo para diferença
  - Diferença entre pessoas com bournour
  - Qualidade de vida
  - Empregos/Cargos que causam bournout
  - Faixa etária
- Criação do Dashboard
- Apresentação
  - Justificativa da correlação entre dados
  - Descoberta do porque tal comportamento acontece através dos dados encontrados

> Como variou a taxa de notificações de síndrome de burnout por 100 mil habitantes entre 2020 e 2025 em São Paulo, Minas Gerais, Distrito Federal e na UF de menor taxa, e como essa variação se distribui por faixa etária e sexo?
> “Proporção populacional não interfere na taxa” só vale se vocês realmente calcularem a taxa com a população (IBGE) como denominador. Com contagem bruta, a população interfere sim.

## Diário de bordo

03/10/2026 - Primeira reúnião. Discusão de ideias, 2 temas principais
15/10/2026 - ETAPA 1 - Definimos o tema, perguntas, público, território, período, fonte oficial e ODS com meta específica. Acesso aos dados da base oficial e conversão de DBC para CSV (visualizar os dados do Datasus)
16/10/2026 - ETAPA 2 - Iniciamos a tentativa de escolher o que vamos mostrar, procurar saber o que são os códigos nas tabelas, procuramos uma forma de filtrar os dados (pensamos em programação ou excel) 

---

O que desenvolver - Etapa 1
Delimitar um problema social observável, formular pergunta respondível com dados, indicar público,
território, período, fonte oficial e ODS com meta específica. Elaborar contrato de equipe (objetivos,
tarefas, reuniões, solução de impasses).

• ODS Principal: ODS 3 – Saúde e Bem-Estar.
• Meta Específica (Meta 3.4): "Até 2030, reduzir em um terço a mortalidade prematura por doenças não transmissíveis via prevenção e tratamento, e promover a saúde mental e o bem-estar."
• ODS Complementar (Diferencial para o grupo): ODS 8 – Trabalho Decente e Crescimento Econômico.
• Meta Específica (Meta 8.8): "Proteger os direitos trabalhistas e promover ambientes de trabalho seguros e protegidos para todos os trabalhadores..."
• Fontes Oficiais para Coleta de Dados:
• Ministério da Previdência Social / INSS: Para os dados de concessão de benefícios por incapacidade temporária (antigo auxílio-doença) motivados por transtornos mentais e comportamentais relacionados ao trabalho.
• MTE (Ministério do Trabalho e Emprego) / SmartLab: Ferramenta governamental que compila dados de acidentes e adoecimentos no trabalho por município.

📊 Desenhando a "Pergunta Respondível" (Ajuste as lacunas em colchetes)

Como o Burnout afeta diferentes categorias, o grupo precisa escolher um público e uma cidade para investigar. Escolham o cenário que acharem mais fácil de pesquisar ou que mais chame a atenção do grupo:

Opção 1: Foco em Profissionais da Saúde (Médicos, Enfermeiros, Técnicos)

"Qual foi o volume de afastamentos do trabalho por Síndrome de Burnout e episódios depressivos registrados entre os profissionais de enfermagem da rede pública hospitalar do município de [Nome da Cidade] no período de [Ex: 2023 a 2025]?"

Opção 2: Foco em Professores (Rede Pública ou Privada)

"Como evoluiu o número de licenças médicas concedidas a professores da rede estadual de ensino de [Nome do Estado] decorrentes de esgotamento profissional (Burnout) entre os anos de [Ex: 2022 e 2025]?"

Opção 3: Foco Geral no Mercado Corporativo/Trabalho Formal da Cidade

"Quais foram as principais causas de afastamento previdenciário (B31 e B91) ligadas a transtornos mentais e do comportamento relacionados ao trabalho no município de [Nome da Cidade] no ano de [Ex: 2025]?"

📝 Resumo dos Dados de Escopo (Checklist da Etapa 1)

Para o documento de vocês, a estrutura de texto direto ficará assim:
• Problema Social: O crescimento dos casos de esgotamento profissional Crônico (Burnout) e o consequente afastamento de trabalhadores de suas atividades laborais.
• Público: [Definam aqui: ex: Professores, Enfermeiros, Trabalhadores formais em geral].
• Território: [A cidade de vocês ou o estado].
• Período: [Definam uma janela de tempo, ex: de 2023 a 2025].
• Fonte Oficial: Dados de afastamento do INSS / Ministério da Previdência Social.
Para deixar essa pergunta pronta para entrega: qual é a profissão/público que vocês querem analisar e em qual cidade ou região vocês estão?


## Etapa 1

Pergunta: Como variou a taxa de notificações de síndrome de burnout por 100 mil habitantes entre 2020 e 2025 em São Paulo, Minas Gerais, Distrito Federal e na UF de menor taxa, e como essa variação se distribui por faixa etária e sexo?

São Paulo - Mai1
Minas Gerais
Distrito Federal



## Etapa 3

- Comparar territórios, períodos ou grupos
- Justificar métricas
- Produzir no mínimo quatro visualizações com títulos, unidades, fonte e interpretação.
- Relacionar resultados à pergunta e ao ODS
- Formular proposta i\nicial de ação

### Gráficos para fazer

- Evolução anual de Diagnótico por Estado - **Gráfico de linha**
  - São Paulo (2020-2025)
  - Minas Gerais (2020-2025)
  - Distrito Federal (2020-2025)
- Idade
  - Índice de diagnóstico por idade **Gráfico**
- Sexo
  - Qual sexo tem mais probabilidade de burnout? **Gráfico**
- Profissão 5 principais
  - Tempo de permanência no trabalho atual **Gráfico**

### Justificar métricas

- Evolução anual de Diagnótico por Estado
  - São Paulo (Oportunidade de trabalho e população elevada)
  - Minas Gerais (Qualidade de vida)
  - Distrito Federal (Capital, está ligado à natureza da pressão e à cultura organizacional, e não ao tamanho do território ou ao valor do salário)
- Idade (Qual faixa etária possui mais índices de burnout?)
- Sexo (verificar como os casos de Burnout estão distribuídos entre os gêneros e investigar possíveis relações com jornada de trabalho, responsabilidades familiares e condições profissionais. Escolhemos a métrica gênero para comparar a distribuição dos casos de Burnout entre diferentes grupos e identificar possíveis diferenças nos padrões de esgotamento profissional.)
- Profissões e o tempo de permanência (identificar quais profissões tem mais diagnóticos por burnout e medir se o fator do tempo influência no indice)

## Relacionar resultados à pergunta e ao ODS

Como variou a taxa de notificações de síndrome de burnout por 100 mil habitantes entre 2020 e 2025 em São Paulo, Minas Gerais, Distrito Federal e na UF de menor taxa, e como essa variação se distribui por faixa etária e sexo?

**Meta 3.4 (principal)**: até 2030, reduzir em um terço a mortalidade prematura por doenças não transmissíveis, por meio de prevenção e tratamento, e promover a saúde mental e o bem-estar. O burnout não é medido pelos indicadores oficiais dessa meta (3.4.1 e 3.4.2), então ela entra como referência de contexto: acompanhar as notificações mostra se a saúde mental do trabalhador está sendo vista pelo sistema de saúde.

**Meta 8.8 (complementar)**: proteger os direitos trabalhistas e promover ambientes de trabalho seguros para todos os trabalhadores. Ela liga o burnout às condições de trabalho. A meta 8.5 (pleno emprego e igualdade de remuneração) foi retirada, porque a base não tem dados de renda ou emprego.

## Formular proposta inicial de ação

Colocar mais ongs ou centros de tratamento em locais com mais taxas
Psicologos
Aplicativo identificação de burnout90
programa saude da familia - checkup

fatores estressores de burnout
Quais capitais tem programa saude da familia
burnout é qualidade de vida

