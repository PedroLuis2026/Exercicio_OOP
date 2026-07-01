import os 
from rich import print
from rich.table import Table
os.system("cls" if os.name == "nt" else "clear")

class Produto:
    def __init__(self, nome, quantidade, preço):
        self.nome = nome
        self.quantidade = quantidade
        self.preço = preço

    def adicionar_estoque(self, qtd):
        self.quantidade += qtd

    def remover_estoque(self, qtd):
        self.quantidade -= qtd

    def exibir(self):
        preço_f = f"R${self.preço:.2f}".replace(".", ",")
        if self.quantidade <= 30:
            cor = "[red]"
        elif 30 < self.quantidade <= 50:
            cor = "[yellow]"
        else:
            cor = "[aquamarine3]"
        tabela = Table(title= "[grey39]Tabela do produto[/]") 
        tabela.add_column(f"[gold3]{self.nome}[/]")
        tabela.add_column("[light_green]Preço[/]", style = "green")
        tabela.add_row(f"{cor}{self.quantidade}[/]", f"{preço_f}")
        print(tabela)

p1 = Produto("Queijo Coalho", 0, 10.50)
p1.adicionar_estoque(100)
p1.exibir()