# Mercado Livre CrewAI

Gerador automatizado de anúncios otimizados para o Mercado Livre utilizando múltiplos agentes de IA com CrewAI. O sistema pesquisa preços, analisa o mercado, coleta especificações técnicas e cria um anúncio completo e otimizado para SEO.

## Como funciona

O projeto utiliza 4 agentes especializados que trabalham em sequência:

```
Pesquisador de Preços ──┐
                        ├──► Analista de Mercado ────► Criador de Anúncio
Especialista em Produto─┘                          
                                                   
```

| Agente | Função | Ferramentas |
|---|---|---|
| **Pesquisador de Preços** | Busca onde o produto é vendido no Brasil e coleta preços (Mercado Livre, Amazon, Shopee, etc.) | SerperDevTool |
| **Analista de Mercado** | Calcula preços mín/méd/máx, avalia nível de demanda e concorrência | — |
| **Especialista em Produto** | Coleta especificações técnicas completas (dimensões, materiais, compatibilidade, diferenciais) | SerperDevTool |
| **Criador de Anúncio** | Monta o anúncio final otimizado com título, descrição persuasiva e chamada para ação | — |

### Saída gerada

O anúncio final contém:
- Título otimizado (máx. 60 caracteres)
- Preço médio de mercado encontrado
- Nível de demanda e concorrência
- Descrição persuasiva com especificações técnicas
- Chamada para ação

## Requisitos

- Python 3.10+
- Conta na [Serper API](https://serper.dev) (para buscas web)
- GitHub Token com acesso ao modelo `openai/gpt-4o-mini` via Azure inference

## Instalação

```bash
git clone <url-do-repositorio>
cd mercado_livre_crewai

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

pip install -r requirements.txt
```

## Configuração

Copie o arquivo de exemplo e preencha com suas credenciais:

```bash
copy .env.exemple .env
```

Edite o `.env`:

```env
GITHUB_TOKEN=seu_github_token_aqui
SERPER_API_KEY=sua_chave_serper_aqui
```

> `GITHUB_TOKEN` é usado como chave de autenticação no endpoint Azure de inferência do modelo `gpt-4o-mini`.

## Uso

```bash
python main.py
```

O sistema pedirá as informações do produto:

```
Digite as informações do produto: iPhone 15 Pro Max 256GB
```

Após alguns instantes, o anúncio gerado será exibido no terminal:

```
========== ANÚNCIO GERADO ==========

[Anúncio completo e otimizado para o Mercado Livre]
```

## Dependências

```
crewai
crewai_tools
python-dotenv
```

## Estrutura do projeto

```
mercado_livre_crewai/
├── main.py          # Ponto de entrada — lê input do usuário e exibe resultado
├── crew.py          # Orquestração da equipe de agentes
├── agents.py        # Definição dos 4 agentes e configuração do LLM
├── tasks.py         # Definição das 4 tarefas e dependências entre elas
├── requirements.txt # Dependências Python
└── .env.exemple     # Template de variáveis de ambiente
```
