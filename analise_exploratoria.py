import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("internacoes_sc.csv")
df["Data"] = pd.to_datetime(df["Data"])

# Gráfico de tendência
plt.figure(figsize=(10, 6))
plt.plot(df["Data"], df["Qtd. internacoes"])
plt.title("Tendência do Número de Internações em SC (2010-2022)")
plt.xlabel("Ano")
plt.ylabel("Número de Internações")
plt.grid(True)
plt.show()

# Média e o desvio padrão das internações anuais
media_anual = df.groupby(df["Data"].dt.year)["Qtd. internacoes"].mean()
desvio_padrao_anual = df.groupby(df["Data"].dt.year)["Qtd. internacoes"].std()

print(f"Média anual de internações:\n{media_anual}")
print(f"Desvio padrão anual de internações:\n{desvio_padrao_anual}")
