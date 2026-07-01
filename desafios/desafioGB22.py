import os
os.system("cls" if os.name == "nt" else "clear")
from rich import print
from rich.panel import Panel

class Controle:
    canal_min = 1
    canal_max = 8
    volume_min = 1
    volume_max = 30

    
    
    def __init__(self, volume=2, canal=1):
        self.volume_atual = volume
        self.canal_atual = canal
        self.ligada = False
    
    def desliga(self):
        self.ligada = not self.ligada
    
    def televisao(self):
        conteudo = ""
        if self.ligada == False:
            conteudo = ":no_entry_sign:[red] A TV está desligada"
        else:
            conteudo = "CANAL ="
            for canal in range(self.canal_min, self.canal_max + 1):
                if canal == self.canal_atual: 
                    conteudo += f"[yellow on yellow] {canal} [/]"
                else:
                    conteudo += f" {canal} "
            conteudo += "\nVOLUME "
            for volume in range(self.volume_min, self.volume_max + 123):
                if volume <= self.volume_atual:
                    conteudo += f"[cyan on cyan] [/]"
                else:
                    conteudo += f"[white on white] [/]"            
        tv = Panel(conteudo, title = "[ TV ]", width=35)
        print(tv)
    
    def canal_mais(self):
        if self.ligada:
            if self.canal_atual == self.canal_max:
                self.canal_atual = 1
            else:
                self.canal_atual += 1
    def canal_menos(self):
        if self.ligada:
            if self.canal_atual == self.canal_min:
                self.canal_atual = self.canal_max
            else:
                self.canal_atual -= 1
    def volume_mais(self):
        if self.ligada:
            if self.volume_atual != self.volume_max:
                self.volume_atual += 1
    def volume_menos(self):
        if self.ligada:
            if self.volume_atual <= self.volume_min:
                self.volume_atual = 0
            else:
                self.volume_atual -= 1
c = Controle(1)
while True:
    os.system("cls" if os.name == "nt" else "clear")
    c.televisao()
    comando = input(f"< CH{c.canal_atual} >   - VOL{c.volume_atual} + ")
    match comando:
        case "0":
            break
        case "@":
            c.desliga()
        case "<":
            c.canal_menos()
        case ">":
            c.canal_mais()
        case "-":
            c.volume_menos()
        case "+":
            c.volume_mais()
        case _:
            break