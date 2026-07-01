import os 
from rich import print
from rich.panel import Panel
from rich.console import Console
os.system("cls" if os.name == "nt" else "clear")
console = Console()
class Tarefa:
    def __init__(self,descricao="",prioridade="Baixa"):
        self.descricao = descricao.capitalize()
        self.prioridade = prioridade.capitalize()
        self.adicionais = []

    def tarefas_adicionais(self):
        self.adicionais.append(console.input("[bold grey69]Digite uma tarefa adicional: [/]").strip().capitalize())
   
    def exibir_tarefa(self):
        if self.prioridade == "Baixa":
            cor = "chartreuse3"
        elif self.prioridade == "Média":
            cor = "yellow3"
        else:
            cor = "red1"
        mensagem = f"{self.descricao}"
        p = f"\n".join(f"• {item}" for item in self.adicionais)
        if len(self.adicionais) == 0:
            p = "Nenhuma tarefa adicional foi adicionada!"
        print(Panel(f"[bold]{mensagem}[/]\n\n"
                    f"[bold]ADICIONAIS:[/]\n[gold3]{p}[/]",title="- TAREFAS -",border_style=f"{cor}", style="grey69", expand=False))

tarefas = Tarefa("Eu tenho que estudar hoje bastante POO hoje!", "alta")
tarefas.tarefas_adicionais()
tarefas.tarefas_adicionais()
tarefas.exibir_tarefa()
