import os
from crewai import Agent, LLM
from crewai_tools import SerperDevTool

def criar_llm():
    return LLM(
        model="openai/gpt-4o-mini",
        api_key=os.getenv("GITHUB_TOKEN"),
        base_url="https://models.inference.ai.azure.com"
    )

def criar_agentes(llm):
    busca = SerperDevTool()

    pesquisador = Agent(
        role="Pesquisador de Preços",
        goal="Encontrar onde o produto é vendido no Brasil e quais os preços praticados",
        backstory="Especialista em coleta de dados de e-commerce brasileiro.",
        llm=llm,
        tools=[busca],
        verbose=False
    )

    analista = Agent(
        role="Analista de Mercado",
        goal="Calcular preço médio e avaliar nível de demanda do produto",
        backstory="Especialista em análise de dados de mercado e comportamento do consumidor.",
        llm=llm,
        verbose=False
    )

    especialista_produto = Agent(
        role="Especialista em Produto",
        goal="Levantar especificações técnicas completas do produto",
        backstory="Especialista em fichas técnicas e catalogação de produtos para e-commerce.",
        llm=llm,
        tools=[busca],
        verbose=False
    )

    montador_anuncio = Agent(
        role="Criador de Anúncios",
        goal="Montar anúncio completo e otimizado com base em todas as informações coletadas",
        backstory="Copywriter e especialista em SEO para Mercado Livre.",
        llm=llm,
        verbose=False
    )

    return pesquisador, analista, especialista_produto, montador_anuncio
