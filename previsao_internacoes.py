import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("internacoes_sc.csv")
df["Data"] = pd.to_datetime(df["Data"])

# Features
df["Ano"] = df["Data"].dt.year
df["Mês"] = df["Data"].dt.month

# Dividir os dados em treinamento e teste
X = df[["Ano", "Mês"]]
y = df["Qtd. internacoes"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsão para janeiro de 2023
ano_2023 = np.array([[2023, 1]])
previsao = model.predict(ano_2023)

print(f"Previsão de internações para janeiro de 2023: {previsao[0]:.0f}")

