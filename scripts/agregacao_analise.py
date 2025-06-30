import pandas as pd

# Leitura dos arquivos tratados
df_sg = pd.read_csv('data/processed/sindrome_gripal_tratada.csv', encoding='latin1')
df_ciano = pd.read_csv('data/processed/cianobacterias_tratada.csv', encoding='latin1')

# Conversão de datas
df_sg['dataNotificacao'] = pd.to_datetime(df_sg['dataNotificacao'])
df_ciano['Data da Coleta'] = pd.to_datetime(df_ciano['Data da Coleta'])

# Padronização dos nomes de município
df_sg['municipio'] = df_sg['municipio'].str.strip().str.upper()
df_ciano['Município'] = df_ciano['Município'].str.strip().str.upper()

# Agrupamentos por mês e município
df_sg['ano_mes'] = df_sg['dataNotificacao'].dt.to_period('M')
df_sg_grouped = df_sg.groupby(['municipio', 'ano_mes']).size().reset_index(name='casos_sg')

df_ciano['ano_mes'] = df_ciano['Data da Coleta'].dt.to_period('M')
df_ciano_grouped = df_ciano.groupby(['Município', 'ano_mes'])['Resultado'].mean().reset_index(name='media_resultado_ciano')

# Merge com chaves padronizadas
df_merge = pd.merge(
    df_sg_grouped,
    df_ciano_grouped,
    left_on=['municipio', 'ano_mes'],
    right_on=['Município', 'ano_mes'],
    how='inner'
)

# Drop da coluna duplicada
df_merge = df_merge.drop(columns=['Município'])

# Exporta para CSV
df_merge.to_csv('data/processed/base_agregada.csv', index=False, encoding='latin1')
