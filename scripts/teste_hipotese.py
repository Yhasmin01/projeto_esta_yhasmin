import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

# Lê a base agregada
df = pd.read_csv('data/processed/base_agregada.csv', encoding='latin1')

# Remove valores ausentes
df = df.dropna(subset=['media_resultado_ciano', 'casos_sg'])

# Verifica se há variedade suficiente para fazer qcut
if df['media_resultado_ciano'].nunique() > 1 and df['casos_sg'].nunique() > 1:
    df['nivel_ciano'] = pd.qcut(df['media_resultado_ciano'], q=2, labels=['baixo', 'alto'], duplicates='drop')
    df['nivel_casos'] = pd.qcut(df['casos_sg'], q=2, labels=['baixo', 'alto'], duplicates='drop')

    # Tabela de contingência
    contingencia = pd.crosstab(df['nivel_ciano'], df['nivel_casos'])

    # Teste qui-quadrado
    chi2, p, dof, expected = chi2_contingency(contingencia)

    print("Tabela de contingência:")
    print(contingencia)
    print(f"\nValor de p: {p:.4f}")

    if p < 0.05:
        print("Há evidências de associação entre nível de cianobactérias e casos de síndrome gripal.")
    else:
        print("Não há evidências de associação entre nível de cianobactérias e casos de síndrome gripal.")

    # Gráfico de calor
    sns.heatmap(contingencia, annot=True, fmt="d", cmap="YlGnBu")
    plt.title("Mapa de calor da associação entre cianobactérias e casos SG")
    plt.savefig("images/grafico_associacao.png")
    plt.show()
else:
    print("Não há variabilidade suficiente para aplicar qcut.")
