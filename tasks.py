from crewai import Task

def criar_tarefas(produto, pesquisador, analista, especialista_produto, montador_anuncio):

    tarefa_pesquisa = Task(
        description=(
            f"Pesquise no Brasil onde o seguinte produto é vendido e quais os preços:\n\n{produto}\n\n"
            "Busque em lojas como Mercado Livre, Amazon, Shopee e outras.\n"
            "Liste os preços encontrados e as lojas."
        ),
        expected_output=(
            "Lista com: nome das lojas onde é vendido e os preços encontrados em R$."
        ),
        agent=pesquisador
    )

    tarefa_analise = Task(
        description=(
            "Com base nos preços coletados na pesquisa:\n"
            "1) Calcule o preço mínimo, máximo e médio em R$\n"
            "2) Avalie a demanda: alta (muitos vendedores), média ou baixa (poucos vendedores)\n"
            "3) Avalie o nível de concorrência\n"
        ),
        expected_output=(
            "Relatório com: preço mínimo, médio e máximo em R$, "
            "nível de demanda e nível de concorrência."
        ),
        agent=analista,
        context=[tarefa_pesquisa]  # lê o resultado da pesquisa
    )

    tarefa_especificacoes = Task(
        description=(
            f"Pesquise e levante as especificações técnicas do produto:\n\n{produto}\n\n"
            "Inclua: dimensões, peso, materiais, funcionalidades, compatibilidades e diferenciais."
        ),
        expected_output=(
            "Ficha técnica completa com todas as especificações do produto."
        ),
        agent=especialista_produto
    )

    tarefa_anuncio = Task(
        description=(
            f"Monte o anúncio completo para Mercado Livre do produto:\n\n{produto}\n\n"
            "Use todas as informações coletadas anteriormente e inclua obrigatoriamente:\n"
            "1) Título otimizado (máximo 60 caracteres)\n"
            "2) Preço médio de mercado encontrado\n"
            "3) Nível de demanda do produto\n"
            "4) Descrição persuasiva com especificações técnicas\n"
            "5) Chamada para ação final\n"
        ),
        expected_output=(
            "Anúncio final completo com título, análise de mercado (preço médio e demanda) "
            "e descrição otimizada. Sem emojis."
        ),
        agent=montador_anuncio,
        context=[tarefa_analise, tarefa_especificacoes]  # lê os dois resultados
    )

    return tarefa_pesquisa, tarefa_analise, tarefa_especificacoes, tarefa_anuncio
