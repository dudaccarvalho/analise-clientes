
-- ==============================================
-- PROJETO: ANÁLISE DE CLIENTES E RETENÇÃO
-- Autora: Maria Eduarda Carvalho
-- Banco de dados: PostgreSQL
-- Dados fictícios para portfólio
-- ==============================================

-- 1. VISÃO GERAL DOS CLIENTES

SELECT
    COUNT(*) AS total_clientes,
    SUM(cancelou) AS clientes_cancelados,
    ROUND(AVG(cancelou::NUMERIC) * 100, 2)
        AS taxa_cancelamento,
    ROUND(
        SUM(
            CASE
                WHEN cancelou = 0 THEN valor_mensal
                ELSE 0
            END
        ), 2
    ) AS receita_mensal_ativa
FROM public.clientes;


-- 2. TAXA DE CANCELAMENTO POR PLANO

SELECT
    plano,
    COUNT(*) AS total_clientes,
    SUM(cancelou) AS cancelamentos,
    ROUND(AVG(cancelou::NUMERIC) * 100, 2)
        AS taxa_cancelamento
FROM public.clientes
GROUP BY plano
ORDER BY taxa_cancelamento DESC;


-- 3. CANCELAMENTO POR NÍVEL DE ENGAJAMENTO

SELECT
    CASE
        WHEN acessos_mes < 20 THEN 'Baixo'
        WHEN acessos_mes < 50 THEN 'Médio'
        ELSE 'Alto'
    END AS nivel_engajamento,
    COUNT(*) AS total_clientes,
    SUM(cancelou) AS cancelamentos,
    ROUND(AVG(cancelou::NUMERIC) * 100, 2)
        AS taxa_cancelamento
FROM public.clientes
GROUP BY nivel_engajamento
ORDER BY taxa_cancelamento DESC;


-- 4. SATISFAÇÃO MÉDIA DOS CLIENTES

SELECT
    CASE
        WHEN cancelou = 1 THEN 'Cancelado'
        ELSE 'Ativo'
    END AS status_cliente,
    ROUND(AVG(satisfacao), 2) AS satisfacao_media,
    COUNT(*) AS total_clientes
FROM public.clientes
GROUP BY cancelou;


-- 5. CLIENTES COM BAIXO ENGAJAMENTO

SELECT
    cliente_id,
    plano,
    acessos_mes,
    meses_cliente,
    satisfacao
FROM public.clientes
WHERE cancelou = 0
  AND acessos_mes < 20
ORDER BY acessos_mes ASC;


-- 6. RECEITA MENSAL ATIVA ESTIMADA POR PLANO

SELECT
    plano,
    COUNT(*) AS clientes_ativos,
    ROUND(SUM(valor_mensal), 2)
        AS receita_mensal_estimada
FROM public.clientes
WHERE cancelou = 0
GROUP BY plano
ORDER BY receita_mensal_estimada DESC;
