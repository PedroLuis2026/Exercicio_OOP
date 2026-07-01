from rich import print
from rich.table import Table

tabela = Table(title="Tabela de preços")

tabela.add_column("[dark_blue]Nome[/]", justify="center", style="red")
tabela.add_column("[light_green]Preço[/]", justify="left", style="green")
tabela.add_row("Lápis", "R$1,50")
tabela.add_row("Borracha", "R$2,00")

print(tabela)