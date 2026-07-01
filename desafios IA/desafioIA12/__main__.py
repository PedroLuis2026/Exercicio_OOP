from rpg import *
import os
os.system("cls" if os.name == "nt" else "clear")
from rich import print

def main():
    # --- ÁREA DE TESTES (Sessão do RPG) ---

    print("[bold]=== Manifestação do Outro Lado ===[/]\n")

# Criando os monstros com nome e pontos de vida
    zumbi_sangue = CriaturaSangue("Zumbi de Sangue", 45)
    existencia = CriaturaConhecimento("Anomalia de Conhecimento", 60)

# Invocando a presença deles na mesa
    zumbi_sangue.manifestar_presenca()
    existencia.manifestar_presenca()

if __name__ == "__main__":
    main()