import os
os.system("cls" if os.name == "nt" else "clear")
from logistica import *

def main():
    print("[bold blue]=== Testando VEM Estudante ===[/]")
    vem_estudante = CartaoEstudante("12345", 5.00)
    vem_estudante.descontar_viagem() # Viagem 1: Passa (Sobra 2,45)
    vem_estudante.descontar_viagem() # Viagem 2: Bloqueia (Saldo 2,45 é menor que 2,55)

    print("\n" + "-"*60 + "\n")

    print("[bold blue]=== Testando VEM Comum ===[/]")
    vem_comum = CartaoComum("54321", 10.00)
    vem_comum.descontar_viagem() # Viagem 1: Passa (Sobra 4,90)
    vem_comum.descontar_viagem() # Viagem 2: Bloqueia (Saldo 4,90 é menor que 5,10)

if __name__ == "__main__":
    main()