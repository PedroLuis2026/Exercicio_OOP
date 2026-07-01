import os
from rich import print
from rich.panel import Panel
import keyboard
from rich.live import Live
from rich.console import Group
from rich.progress import Progress, TextColumn, BarColumn, TaskProgressColumn
os.system("cls" if os.name == "nt" else "clear")
from time import sleep

class Lampada:
    def __init__(self, comodo="Nenhum", intensidade=0):
        self.comodo = comodo
        self.intensidade_max = 100
        self.ligada = False
        self.intensidade = intensidade
        self.cor = "white" 
    
    def ligar(self):
        self.ligada = not self.ligada
    
    def status(self):
        if self.ligada is False:
            return Panel("[grey27]A lampâda está desligada[/]",border_style="grey37",title="[grey27]- DESLIGADA -[/]")
        
        if self.intensidade >= 50:
            self.cor = "khaki1"
        elif 25 <= self.intensidade < 50:
            self.cor = "wheat1"
        elif self.intensidade < 25:
            self.cor = "cornsilk1"
        
        if self.intensidade < 0:
            self.intensidade = 0
        if self.intensidade > self.intensidade_max:
            self.intensidade = self.intensidade_max

        progressao = Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(complete_style=self.cor),
            TaskProgressColumn(text_format="[{task.completed_style}]{task.percentage:>3.0f}%")
        )  
        progressao.add_task(f"[{self.cor}]BRILHO[/]", total=self.intensidade_max, completed=self.intensidade)
        conteudo = Group(
            f"[bold grey69]COMÔDO: {self.comodo}[/]\n"
            f"[bold grey69]PORCENTAGEM DA LÂMPADA: [/]",
            progressao
        )
        return Panel(conteudo,border_style="light_goldenrod1",title="[light_goldenrod1]- LIGADA -[/]")
    
    def ajustar_brilho(self, n):
        self.intensidade = n  

l1 = Lampada("Casa", 20)
with Live(l1.status(), refresh_per_second=10) as live:
    while True:
        live.update(l1.status())

        if keyboard.is_pressed('l'):
            l1.ligar()
        if keyboard.is_pressed('esc'):
            break
        sleep(0.1)
