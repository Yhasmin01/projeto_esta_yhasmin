import pandas as pd
import os

base_sg_path = 'data/raw/sindrome_gripal_sp.csv'
base_ciano_path = 'data/raw/vigilancia_cianobacterias_cianotoxinas.csv'

df_sg = pd.read_csv(base_sg_path, sep=';', low_memory=False, encoding='latin1')
df_sg.columns = df_sg.columns.str.strip()
df_sg = df_sg[['municipio', 'dataNotificacao', 'classificacaoFinal']].copy()
df_sg['dataNotificacao'] = pd.to_datetime(df_sg['dataNotificacao'], errors='coerce')
df_sg = df_sg.dropna(subset=['dataNotificacao'])

df_ciano = pd.read_csv(base_ciano_path, sep=';', low_memory=False, encoding='latin1')
df_ciano.columns = df_ciano.columns.str.strip()
df_ciano = df_ciano[['Município', 'Data da Coleta', 'Resultado']].copy()
df_ciano['Data da Coleta'] = pd.to_datetime(df_ciano['Data da Coleta'], errors='coerce')
df_ciano['Resultado'] = df_ciano['Resultado'].replace(',', '.', regex=True).astype(str)
df_ciano['Resultado'] = pd.to_numeric(df_ciano['Resultado'], errors='coerce')

os.makedirs('data/processed', exist_ok=True)
df_sg.to_csv('data/processed/sindrome_gripal_tratada.csv', index=False, encoding='latin1')
df_ciano.to_csv('data/processed/cianobacterias_tratada.csv', index=False, encoding='latin1')
