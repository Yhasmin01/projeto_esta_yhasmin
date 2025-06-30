import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("imagens", exist_ok=True)

df = pd.read_csv('data/processed/base_agregada.csv', encoding='latin1')

plt.figure(figsize=(8, 5))
plt.scatter(df['media_resultado_ciano'], df['casos_sg'], alpha=0.5)
plt.title('Dispersão - Cianobactérias vs Casos SG')
plt.xlabel('Média de Cianobactérias')
plt.ylabel('Casos de Síndrome Gripal')
plt.tight_layout()
plt.savefig('imagens/dispersao_ciano_sg.png')
plt.close()