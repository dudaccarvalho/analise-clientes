
import pandas as pd

# 1. Carregar os dados
df = pd.read_csv("clientes.csv")

print("\n=== VISÃO GERAL ===")
print(df.head())

print("\n=== QUALIDADE DOS DADOS ===")
print("Total de registros:", len(df))
print("Clientes duplicados:", df["cliente_id"].duplicated().sum())
print("Valores ausentes:")
print(df.isnull().sum())

# 2. Indicadores gerais
total_clientes = len(df)
clientes_cancelados = df["cancelou"].sum()
taxa_cancelamento = df["cancelou"].mean() * 100
faturamento_ativo = df.loc[
    df["cancelou"] == 0, "valor_mensal"
].sum()

print("\n=== INDICADORES GERAIS ===")
print(f"Total de clientes: {total_clientes}")
print(f"Clientes cancelados: {clientes_cancelados}")
print(f"Taxa de cancelamento: {taxa_cancelamento:.2f}%")
print(f"Receita mensal ativa estimada: R$ {faturamento_ativo:.2f}")

# 3. Cancelamento por plano
print("\n=== CANCELAMENTO POR PLANO ===")
cancelamento_plano = (
    df.groupby("plano")["cancelou"]
    .agg(["count", "sum", "mean"])
    .rename(columns={
        "count": "total_clientes",
        "sum": "cancelamentos",
        "mean": "taxa_cancelamento"
    })
)

cancelamento_plano["taxa_cancelamento"] *= 100
print(cancelamento_plano.round(2))

# 4. Engajamento dos clientes
print("\n=== ACESSOS E CANCELAMENTO ===")

df["faixa_acessos"] = pd.cut(
    df["acessos_mes"],
    bins=[-1, 19, 49, 100],
    labels=["Baixo", "Medio", "Alto"]
)

engajamento = (
    df.groupby("faixa_acessos", observed=True)["cancelou"]
    .agg(["count", "mean"])
)

engajamento["mean"] *= 100
engajamento.columns = ["clientes", "taxa_cancelamento"]

print(engajamento.round(2))

# 5. Satisfação por situação do cliente
print("\n=== SATISFAÇÃO MÉDIA ===")
print(df.groupby("cancelou")["satisfacao"].mean().round(2))

# 6. Exportar os resultados
cancelamento_plano.to_csv(
    "cancelamento_por_plano.csv",
    encoding="utf-8-sig"
)

engajamento.to_csv(
    "cancelamento_por_engajamento.csv",
    encoding="utf-8-sig"
)

print("\nAnálise concluída! Arquivos exportados.")
