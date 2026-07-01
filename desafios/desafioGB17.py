import os
os.system("cls" if os.name == "nt" else "clear")
from rich import print
from rich.panel import Panel
from rich.traceback import install

install()


class Produto:

    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def etiqueta(self):
        nome_centralizado = self.nome.center(30)
        conteudo = f"[grey37]{nome_centralizado}[/]\n"
        conteudo += f"{"-" * 30}"

        preço_f = f"{self.preço:,.2f}".replace(".",",")
        largura_total = 30
        espaços_vazios = largura_total - len(preço_f)
        lado_esquerdo = espaços_vazios / 2
        lado_direito = espaços_vazios - lado_esquerdo

        preço_linha = (
            f"{"." * int(lado_esquerdo)}" +
            f"[bright_green]{preço_f}[/]" +
            f"{"." * int(lado_direito)}"
        )
        conteudo += preço_linha
        etiqueta = Panel(conteudo, title= "[bright_yellow]Etiqueta[/]", width= 34)
        print(etiqueta)

p1 = Produto("Iphone 16 Pro Max", 4000.00)
p2 = Produto ("Notebook", 180000)
p1.etiqueta()
p2.etiqueta()