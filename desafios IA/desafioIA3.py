import os 
from rich import print
from rich.panel import Panel
from rich.align import Align

os.system("cls" if os.name == "nt" else "clear")

class Conta:
    
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.historico = []
    def depositar(self, valor):
        self.saldo += valor
        valor_f = f"R${valor:.2f}".replace(".", ",")
        self.historico.append(f"[green]+ R${valor:.2f}[/]".replace(".", ","))
        print(Panel(f"Você adicionou {valor_f}:money_bag:", style= "green", border_style="green", expand=False))

    def retirar(self, valor):
        self.saldo -= valor
        valor_f = f"R${valor:.2f}".replace(".", ",")
        self.historico.append(f"[red]- R${valor:.2f}[/]".replace(".", ","))
        print(Panel(f"Você retirou {valor_f}:money_with_wings:", style="yellow", border_style="green", expand=False))

    
    def exibir(self):
        p = ""
        if not self.historico:
            p = "[grey50]Nenhuma movimentação foi feita![/]"
        else:
            p = "\n".join(self.historico)
        saldo_f = f"R${self.saldo}".replace(".", ",")
        print(Panel(f"[bold white]TITULAR:[/][light_goldenrod3]{self.titular}[/]\n"
                    f"[bold white]SALDO ATUAL:[/][green]{saldo_f}[/]\n"
                    f"[bold cyan]MOVIMENTAÇÕES[/]:\n{p}", title="[gold3]- CONTA -[/]", style="grey39", expand=False))

p1 = Conta("Pedro", 10000)
p1.retirar(800)
p1.depositar(400)
p1.retirar(800)
p1.depositar(400)
p1.retirar(800)
p1.depositar(400)
p1.retirar(800)
p1.depositar(400)
p1.exibir()