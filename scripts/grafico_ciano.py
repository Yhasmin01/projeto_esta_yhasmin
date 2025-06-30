import pandas as pd
import matplotlib.pyplot as plt
import os

# Cria pasta de imagens se não existir
os.makedirs("imagens", exist_ok=True)

df = pd.read_csv('data/processed/base_agregada.csv', encoding='latin1')

# Histograma
plt.figure(figsize=(8, 5))
df['media_resultado_ciano'].hist(bins=20)
plt.title('Histograma - Média Cianobactérias')
plt.xlabel('Média de Cianobactérias')
plt.ylabel('Frequência')
plt.tight_layout()
plt.savefig('imagens/histograma_ciano.png')
plt.close()

# Boxplot
plt.figure(figsize=(5, 5))
df.boxplot(column='media_resultado_ciano')
plt.title('Boxplot - Média Cianobactérias')
plt.tight_layout()
plt.savefig('imagens/boxplot_ciano.png')
plt.close()