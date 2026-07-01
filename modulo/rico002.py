from rich import print
from rich.panel import Panel

caixa = Panel("Esse aqui é um painel de exemplo", title="[not italic]Mensagem[/]", style="dark_red italic")

print(caixa)