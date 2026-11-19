
import os
import pandas as pd
import matplotlib.pyplot as plt

# Carregar a base de clientes
df = pd.read_csv("clientes.csv")

# Criar a pasta para salvar os gráficos
os.makedirs("graficos", exist_ok=True)

# Cores do nosso projeto
roxo = "#7952B3"
azul = "#334E68"
verde = "#2A9D8F"

# GRÁFICO 1 — Taxa de cancelamento por plano
plano = (
    df.groupby("plano")["cancelou"]
    .mean()
    .mul(100)
    .sort_values()
)

plt.figure(figsize=(9, 5))
barras = plt.barh(plano.index, plano.values, color=roxo)
plt.title("Taxa de Cancelamento por Plano")
plt.xlabel("Taxa de cancelamento (%)")
plt.xlim(0, 100)
plt.bar_label(barras, fmt="%.1f%%", padding=4)
plt.tight_layout()
plt.savefig("graficos/cancelamento_por_plano.png", dpi=200)
plt.close()

# GRÁFICO 2 — Cancelamento por engajamento
df["faixa_acessos"] = pd.cut(
    df["acessos_mes"],
    bins=[-1, 19, 49, 100],
    labels=["Baixo", "Medio", "Alto"]
)

engajamento = (
    df.groupby("faixa_acessos", observed=True)["cancelou"]
    .mean()
    .mul(100)
)

plt.figure(figsize=(9, 5))
barras = plt.bar(
    engajamento.index.astype(str),
    engajamento.values,
    color=azul
)
plt.title("Cancelamento por Nível de Engajamento")
plt.ylabel("Taxa de cancelamento (%)")
plt.ylim(0, 100)
plt.bar_label(barras, fmt="%.1f%%", padding=4)
plt.tight_layout()
plt.savefig("graficos/cancelamento_por_engajamento.png", dpi=200)
plt.close()

# GRÁFICO 3 — Distribuição de acessos
plt.figure(figsize=(9, 5))
plt.hist(df["acessos_mes"], bins=15, color=verde, edgecolor="white")
plt.title("Distribuição de Acessos Mensais")
plt.xlabel("Número de acessos")
plt.ylabel("Quantidade de clientes")
plt.tight_layout()
plt.savefig("graficos/distribuicao_acessos.png", dpi=200)
plt.close()

print("Gráficos criados com sucesso!")
print("Confira os arquivos na pasta 'graficos'.")
