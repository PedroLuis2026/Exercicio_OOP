import os
os.system("cls" if os.name == "nt" else "clear")
from rich import print


class Caneta:
    def __init__(self,cor = "white"):
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tampa = True
    def destampar(self):
        return self.tampa == False

    def quebrar_linha(self,quantidade):
        quantidade -= 1
        print(f"{"\n" * quantidade}")

    def escrever(self, mensagem):
        if self.tampa: 
            print(f":prohibited: A {self.cor}caneta[/] está tampada.")
        else:
            print(f"{self.cor}{mensagem}[/]", end="")

c1 = Caneta("Azul")
c1.escrever("Olá")
c1.quebrar_linha(3)
c1.escrever("Eu sou Pedro")
        