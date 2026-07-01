import os 
from rich import print
from rich.panel import Panel
os.system("cls" if os.name == "nt" else "clear")

class Livros:
    def __init__(self, titulo, autor, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def emprestar(self):
        if not self.disponivel:
            print(Panel(f"O livro [gold3]{self.titulo}[/] já está indisponível!",style="grey69",border_style="yellow", expand=False))
        else:
            self.disponivel = False
            print(Panel(f"Livro [gold3]{self.titulo}[/] emprestado.",style="grey69",border_style="red3", expand=False))
    def devolver(self):
        if self.disponivel:
            print(Panel(f"O livro [gold3]{self.titulo}[/] já foi devolvido!", style="grey69", border_style="yellow", expand=False))
        else:
            self.disponivel = True
            print(Panel(f"Livro [gold3]{self.titulo}[/] devolvido.",style="grey69",border_style="pale_green1", expand=False))
    def status(self):
        if self.disponivel:
            cor = "green"
        else:
            cor = "red"
        print(Panel(f"[bold]AUTOR:[/][gold3]{self.autor}[/]\n"
                    f"[bold]TÍTULO:[/][gold3]{self.titulo}[/]\n"
                    f"[bold]DISPONIBILIDADE:[/][{cor}]{":open_book: Disponível" if self.disponivel is True else ":closed_book: Indísponivel"}[/]",title="- STATUS -", style="grey69",border_style="honeydew2", expand=False))

l1 = Livros("Pequeno Principe", "Gueguel")
l1.emprestar()
l1.devolver()
l1.status()