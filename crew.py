from crewai import Crew
from agents import criar_llm, criar_agentes
from tasks import criar_tarefas

def rodar(produto):
    llm = criar_llm()
    pesquisador, analista, especialista_produto, montador_anuncio = criar_agentes(llm)
    tarefas = criar_tarefas(produto, pesquisador, analista, especialista_produto, montador_anuncio)

    equipe = Crew(
        agents=[pesquisador, analista, especialista_produto, montador_anuncio],
        tasks=list(tarefas),
        verbose=False
    )

    return equipe.kickoff()
