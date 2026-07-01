import os 
os.system("cls" if os.name == "nt" else "clear")
from inv import *

def main():
    print("[bold]=== Simulando Ataques dos Investigadores ===[/]\n")

# Criando as armas
    bastao = ArmaCorpoCorpo("Bastão com Pregos", 5)
    pistola = ArmaFogo("Pistola .38", 10, municao=2)

# Alvo
    monstro = "Zumbi de Sangue"

# Testando Corpo a Corpo
    bastao.atacar(monstro)

    print("-" * 60)

# Testando Arma de Fogo até acabar a munição
    pistola.atacar(monstro) # Tiro 1 (Gasta munição, dano aleatório + 10)
    pistola.atacar(monstro) # Tiro 2 (Gasta munição)
    pistola.atacar(monstro) # Tiro 3 (Deve avisar que está descarregada)

if __name__ == "__main__":
    main()