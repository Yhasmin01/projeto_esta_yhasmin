import pandas as pd

caminho_gripe = 'data/raw/sindrome_gripal_sp.csv'
caminho_agua = 'data/raw/vigilancia_cianobacterias_cianotoxinas.csv'

# Síndrome Gripal (UTF-8 pode dar erro, então usamos ISO-8859-1)
df_gripe = pd.read_csv(caminho_gripe, sep=';', encoding='ISO-8859-1')

# Cianobactérias
df_agua = pd.read_csv(caminho_agua, sep=';', encoding='ISO-8859-1')


# Nomes das colunas da base de síndrome gripal
print("\nColunas da base de síndrome gripal:")
for coluna in df_gripe.columns:
    print("-", coluna)

# Nomes das colunas da base de cianobactérias
print("\nColunas da base de cianobactérias:")
for coluna in df_agua.columns:
    print("-", coluna)
