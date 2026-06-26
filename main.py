from dotenv import load_dotenv
from crew import rodar

load_dotenv()  # carrega o .env

if __name__ == "__main__":
    produto = input("Digite as informações do produto: ")
    resultado = rodar(produto)
    print("\n========== ANÚNCIO GERADO ==========\n")
    print(resultado)