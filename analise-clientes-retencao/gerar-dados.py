
import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

clientes = []

for i in range(1, 1001):
    plano = random.choice(["Basico", "Premium", "Familia"])
    acessos = random.randint(0, 100)
    meses_cliente = random.randint(1, 36)

    # Simula maior risco de cancelamento para clientes
    # que utilizam pouco a plataforma.
    if acessos < 20:
        prob_cancelamento = 0.65
    elif acessos < 50:
        prob_cancelamento = 0.30
    else:
        prob_cancelamento = 0.08

    cancelou = random.random() < prob_cancelamento

    clientes.append({
        "cliente_id": i,
        "plano": plano,
        "acessos_mes": acessos,
        "meses_cliente": meses_cliente,
        "cancelou": int(cancelou),
        "satisfacao": random.randint(1, 5),
        "valor_mensal": {
            "Basico": 29.90,
            "Premium": 59.90,
            "Familia": 89.90
        }[plano]
    })

df = pd.DataFrame(clientes)

df.to_csv("clientes.csv", index=False, encoding="utf-8-sig")

print("Base de dados criada com sucesso!")
print(f"Total de clientes: {len(df)}")
print(df.head())
