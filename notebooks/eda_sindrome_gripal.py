import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Caminho do arquivo
caminho_arquivo =  'data/raw/sindrome_gripal_sp.csv'

# Lendo com encoding correto e delimitador ;
df = pd.read_csv(caminho_arquivo, sep=';', encoding='utf-8')

# --- Análise geral ---
print("Colunas:", df.columns.tolist())
print("\nTipos de dados:\n", df.dtypes)
print("\nValores nulos por coluna:\n", df.isnull().sum())
print("\nResumo estatístico das idades:\n", df['idade'].describe())

# --- Gráficos iniciais ---
# Distribuição por sexo
sns.countplot(data=df, x='sexo')
plt.title('Distribuição por Sexo')
plt.savefig('../outputs/distribuicao_sexo.png')
plt.clf()

# Distribuição de idade
df['idade'].dropna().astype(int).hist(bins=30)
plt.title('Distribuição de Idade')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.savefig('../outputs/distribuicao_idade.png')
plt.clf()

# Top 10 municípios com mais notificações
top_municipios = df['municipio'].value_counts().head(10)
top_municipios.plot(kind='bar')
plt.title('Top 10 Municípios com Mais Notificações')
plt.ylabel('Número de Casos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../outputs/top_municipios.png')
plt.clf()
