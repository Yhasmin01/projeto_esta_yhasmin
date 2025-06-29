import pandas as pd

# caminho_arquivo = 'data/raw/sindrome_gripal_sp.csv'

# df = pd.read_csv(caminho_arquivo, sep=';', nrows=5)

# print(df.columns.tolist())

caminho_arquivo = 'data/raw/vigilancia_cianobacterias_cianotoxinas.csv'

df = pd.read_csv(caminho_arquivo, sep=';', encoding='latin1', nrows=5)

print(df.columns.tolist())
print(df.head())