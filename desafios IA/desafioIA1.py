import os 
from rich import print
from rich.panel import Panel
os.system("cls" if os.name == "nt" else "clear")



class Aluno:
    def __init__(self, nome, notas, curso):
        self.nome = nome
        self.notas = notas
        self.curso = curso
        self.media = sum(self.notas) / len(self.notas)
    
    def exibir_boletim(self):
        p = ""
        lista_numeros = []
        for n in sorted(self.notas):
            if n >= 7:
                cor_numero = "[green]"
            elif 6 <= n < 7:
                cor_numero = "[yellow]"
            else:
                cor_numero = "[red]"
            n_formatado = f"{cor_numero}{n:.1f}[/]".replace(".", ",")
            lista_numeros.append(n_formatado)
            p = "; ".join(lista_numeros)
        cor = "red" if self.media < 7 else "green"
        print(Panel(f"[grey35]Nome:{self.nome}[/]\n[grey35]Notas:[/]{p}\n[grey35]Média:[/][cor]{"Aprovado" if self.media >= 7 else "Reprovado"}[/]",title= f"- {self.curso} -", style= cor))

guel = Aluno("Miguel", [10,2,10,10,5], "Análise e Desenvolvimento de Sistemas")
guel.exibir_boletim()