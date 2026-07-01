import os
from rich import print
from rich.panel import Panel
from rich.console import Group
os.system("cls" if os.name == "nt" else "clear")
from rich.console import Console

console = Console()

class Pessoa:
    def __init__(self,nome="Desconhecido",peso=0.0,altura=0.1):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.imc = peso/(altura**2)

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)

        if imc > 25:
            cor = "red1"
            mensagem = "Você está acima do seu peso ideal."
        elif 18.5 <= imc <= 25:
            cor = "green"
            mensagem = "Você está no seu peso ideal."
        elif imc < 18.5:
            cor = "yellow"
            mensagem = "Você está abaixo do seu peso ideal."
        
        peso_f = f"{self.peso:.2f}kg".replace(".", ",")
        altura_f = f"{self.altura:.2f}m".replace(".", ",")

        conteudo = Group(
            f"[bold]Nome: {self.nome}[/]\n",
            f"[bold]Peso:[/] [{cor}]{peso_f}[/]\n",
            f"[bold]Altura:[/] [{cor}]{altura_f}[/]\n",
            f"[bold]IMC:[/] [{cor}]{mensagem}[/]\n",
        )
        print(Panel(conteudo,title="- IMC -", style="grey69",border_style=f"{cor}", expand=False))

p1 = Pessoa("Luís Miguel", 38.0, 1.25)
p1.calcular_imc()