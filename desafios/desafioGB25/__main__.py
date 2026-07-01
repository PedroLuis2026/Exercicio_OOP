from transportes import *
import os
os.system("cls" if os.name == "nt" else "clear")
from rich import print
from rich.table import Table
def main():
    dist = 30
    entrega1 = Moto(dist)
    entrega2 = Caminhao(dist)
    entrega3 = Drone(dist)
    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("[bold]Distância[/]", justify="left")
    tabela.add_column("[bold]Tipo[/]", justify="left")
    tabela.add_column("[bold]Frete[/]", justify="left")
    tabela.add_row(f"{dist}Km", f"{type(entrega1).__name__}", entrega1.calc_frete())
    tabela.add_row(f"{dist}Km", f"{type(entrega2).__name__}", entrega2.calc_frete())
    tabela.add_row(f"{dist}Km", f"{type(entrega3).__name__}", entrega3.calc_frete())

    print(tabela)

if __name__ == "__main__":
    main()
