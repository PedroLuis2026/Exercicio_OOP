import os
os.system("cls" if os.name == "nt" else "clear")
from rich import print
from rich.panel import Panel

class Churrasco:

    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quantidade = quantidade

    def informaçoes(self):
        conteudo = ""
        conteudo += f"Analisando [medium_spring_green]{self.titulo}[/] com [blue]{self.quantidade} convidados[/]\n"
        conteudo += "Cada participante comerá [grey37]400g[/] de carne e cada KG custa [green1]R$82,40[/]\n"
        
        recomendado = self.quantidade * 0.4
        custo_total = 82.40 * recomendado
        custo_pessoa = custo_total / self.quantidade
        
        conteudo += f"Recomendo comprar [dark_orange3]{recomendado:.3f}KG[/] de carne\n"
        conteudo += f"O custo total será de [green1]R${custo_total:.2f}[/]\n"
        conteudo += f"Cada pessoa devera pagar [light_goldenrod3]R${custo_pessoa:.2f}[/] para participar."
        painel = Panel(conteudo, title=self.titulo)
        print(painel)

churras = Churrasco("Churras de Lanita", 10)
churras.informaçoes()