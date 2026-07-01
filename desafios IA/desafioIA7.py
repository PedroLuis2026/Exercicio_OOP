import os 
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.progress import Progress, TextColumn, BarColumn, TaskProgressColumn, ProgressBar
from rich.console import Group
from rich.align import Align
from rich.live import Live
from rich.text import Text
import keyboard
from time import sleep
os.system("cls" if os.name == "nt" else "clear")
console = Console()


class Personagem:
    def __init__(self,nome="",classe="",vida=0,mana=0):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.vida_max = vida
        self.vida_min = 0
        self.mana = mana
        self.mana_max = mana
        self.mana_min = 0
        self.corm = "white"
        self.corv = "white"

    def status(self):
        #vida
        if self.vida > self.vida_max * 0.50:
            self.corv = "green"
        elif (self.vida_max * 0.25) < self.vida <= (self.vida_max * 0.50):
            self.corv = "yellow"
        else:
            self.corv = "red1"
        
        #mana
        if self.mana > (self.mana_max * 0.50):
            self.corm = "khaki1"
        elif (self.mana_max * 0.25) < self.mana <= (self.mana_max * 0.50):
            self.corm = "light_goldenrod2"
        else:
            self.corm = "light_salmon1"

        progressov = ProgressBar(
            total=self.vida_max,
            completed=self.vida,
            width=35,
            complete_style=self.corv,
            finished_style=self.corv
        )
        progressom = ProgressBar(
            total=self.mana_max,
            completed=self.mana,
            width=35,
            complete_style=self.corm,
            finished_style=self.corm
        )  
        barra_vida = Group(
            f"  [bold {self.corv}]HP {self.vida}/{self.vida_max}[/]",
            progressov
        )
        barra_mana = Group(
            f"  [bold {self.corm}]PE {self.mana}/{self.mana_max}[/]",
            progressom
        )
        status = Panel("    [bold grey62]4FOR[/]\n"
            "[bold grey62]1DEX :star: 2PRE[/]\n"
            "    [bold grey62]1AGI[/]", border_style="bold gold3", expand=False)
        conteudo = Group(
            f"[bold]PERSONAGEM:[/] [light_goldenrod2]{self.nome}[/]",
            f"[bold]CLASSE:[/] [khaki1]{self.classe}[/]",
            "",
            Align.center(status),
            "",
            barra_vida,
            "",
            barra_mana,
            "",
            f"[bold]Comandos: [+][-] [{self.corv}]Vida[/] | [<][>] [{self.corm}]PE[/] | [ESC] Sair[/]"
        )   

        return Panel(conteudo,title=f"- [bold gold3]FICHA[/] -",border_style="honeydew2",style="grey69",expand=False)

p1 = Personagem("Ferdinando", "Combatente", 28,8 )
os.system("cls" if os.name == "nt" else "clear")

with Live(p1.status(), refresh_per_second=15) as live:
    while True:
        live.update(p1.status())
        #diminuir mana
        if keyboard.is_pressed('<'):
            if keyboard.is_pressed('shift'):
                p1.mana -= 10
            else:
                p1.mana -= 1
            if p1.mana < p1.mana_min: p1.mana = p1.mana_min
        #aumentar mana
        if keyboard.is_pressed('>'):
            if keyboard.is_pressed('shift'):
                p1.mana += 10
            else:
                p1.mana += 1
            if p1.mana > p1.mana_max: p1.mana = p1.mana_max
        #aumentar vida
        if keyboard.is_pressed('+'):
            if keyboard.is_pressed('shift'):
                p1.vida += 10
            else:
                p1.vida += 1
            if p1.vida > p1.vida_max: p1.vida = p1.vida_max
        #diminuir vida
        if keyboard.is_pressed('-'):
            if keyboard.is_pressed('shift'):
                p1.vida -= 10
            else:
                p1.vida -= 1
            if p1.vida < p1.vida_min: p1.vida = p1.vida_min
        if keyboard.is_pressed('esc'):
            break
        sleep(0.2)