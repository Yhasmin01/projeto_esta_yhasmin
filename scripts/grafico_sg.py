import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("imagens", exist_ok=True)

df = pd.read_csv('data/processed/base_agregada.csv', encoding='latin1')

# Histograma
plt.figure(figsize=(8, 5))
df['casos_sg'].hist(bins=20)
plt.title('Histograma - Casos de Síndrome Gripal')
plt.xlabel('Número de Casos')
plt.ylabel('Frequência')
plt.tight_layout()
plt.savefig('imagens/histograma_sg.png')
plt.close()

# Boxplot
plt.figure(figsize=(5, 5))
df.boxplot(column='casos_sg')
plt.title('Boxplot - Casos de Síndrome Gripal')
plt.tight_layout()
plt.savefig('imagens/boxplot_sg.png')
plt.close()