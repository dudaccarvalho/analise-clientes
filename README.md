
# 📊 Análise de Clientes e Retenção

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge)

## 💜 Sobre o Projeto

Este projeto apresenta uma análise exploratória de dados voltada ao comportamento, engajamento e retenção de clientes de uma plataforma digital fictícia.

O objetivo é transformar dados em informações relevantes para a tomada de decisão, utilizando Python para processamento e visualização e PostgreSQL para consultas e análises SQL.

A base utilizada contém **1.000 clientes simulados**, permitindo investigar padrões de cancelamento (churn), frequência de acesso e desempenho dos diferentes planos de assinatura.

## 🎯 Objetivos

- Analisar as taxas de cancelamento de clientes.
- Comparar o comportamento dos usuários por plano.
- Investigar a relação entre engajamento e cancelamento.
- Calcular indicadores de receita mensal.
- Desenvolver consultas SQL para análise de negócio.
- Apresentar os resultados por meio de visualizações.

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Geração e processamento dos dados |
| Pandas | Limpeza, exploração e análise |
| Matplotlib | Visualização de dados |
| PostgreSQL | Banco de dados relacional |
| SQL | Consultas e agregações |
| VS Code | Ambiente de desenvolvimento |

## 📁 Estrutura do Projeto

```text
analise-clientes-retencao/
│
├── gerar_dados.py
├── analise_clientes.py
├── graficos.py
├── analise_clientes.sql
├── clientes.csv
├── cancelamento_por_plano.csv
├── cancelamento_por_engajamento.csv
│
├── graficos/
│   ├── cancelamento_por_plano.png
│   ├── cancelamento_por_engajamento.png
│   └── distribuicao_acessos.png
│
└── README.md
```

## 📈 Indicadores Analisados

Os principais indicadores desenvolvidos foram:

- **Total de clientes:** quantidade de usuários da base.
- **Taxa de cancelamento:** percentual de clientes que cancelaram.
- **Cancelamento por plano:** comparação entre as modalidades de assinatura.
- **Engajamento:** frequência de acesso dos usuários.
- **Satisfação média:** avaliação dos clientes.
- **Receita mensal ativa estimada:** soma das mensalidades dos clientes não cancelados.

## 📊 Visualizações

### 1. Taxa de Cancelamento por Plano

Comparação percentual dos cancelamentos entre os planos Básico, Premium e Família.

![Cancelamento por Plano](graficos/cancelamento_por_plano.png)

### 2. Cancelamento por Nível de Engajamento

Análise da associação entre frequência de acesso e cancelamento.

![Cancelamento por Engajamento](graficos/cancelamento_por_engajamento.png)

### 3. Distribuição de Acessos Mensais

Visualização da distribuição dos clientes conforme a quantidade de acessos realizados.

![Distribuição de Acessos](graficos/distribuicao_acessos.png)

## 🗄️ Análise com PostgreSQL

Os dados foram importados para o PostgreSQL, permitindo desenvolver consultas SQL para análise de indicadores.

**Exemplo: cancelamento por plano**

```sql
SELECT
    plano,
    COUNT(*) AS total_clientes,
    SUM(cancelou) AS cancelamentos,
    ROUND(
        AVG(cancelou::NUMERIC) * 100, 2
    ) AS taxa_cancelamento
FROM clientes
GROUP BY plano
ORDER BY taxa_cancelamento DESC;
```

A consulta utiliza funções de agregação e agrupamento para identificar diferenças nas taxas de cancelamento entre os planos.

## 🔍 Principais Aprendizados

O projeto permitiu aplicar conceitos de:

- Análise exploratória de dados.
- Manipulação de DataFrames com Pandas.
- Cálculo de indicadores de negócio.
- Consultas e agregações SQL.
- Modelagem e armazenamento de dados.
- Construção de gráficos com Matplotlib.
- Interpretação de informações para apoio à tomada de decisão.

## ⚠️ Sobre os Dados

Este projeto utiliza exclusivamente dados fictícios, gerados com Python para fins educacionais e de portfólio.

As probabilidades de cancelamento foram configuradas durante a simulação de acordo com faixas de engajamento. Portanto, as associações identificadas não representam descobertas sobre clientes reais.

## 🚀 Como Executar

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/analise-clientes-retencao.git
cd analise-clientes-retencao
```

Instale as dependências:

```bash
python -m pip install pandas matplotlib
```

Gere os dados:

```bash
python gerar_dados.py
```

Execute a análise:

```bash
python analise_clientes.py
```

Gere os gráficos:

```bash
python graficos.py
```

Para executar as consultas SQL, crie a tabela no PostgreSQL, importe o arquivo `clientes.csv` e execute `analise_clientes.sql`.

## 👩‍💻 Desenvolvido por

**Maria Eduarda Carvalho**

Estudante de Sistemas de Informação | Dados, Business Intelligence e Desenvolvimento de Software

Projeto desenvolvido para fins de estudo, prática e composição de portfólio profissional.
