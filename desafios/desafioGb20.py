import os
os.system("cls" if os.name == "nt" else "clear")
from rich import print
from rich.panel import Panel

class Gamer:
    
    def __init__(self, nome, nick, games=[]):
        self.nome = nome
        self.nick = nick
        self.games = []
    def add_favoritos(self, favorito):
        self.games.append(favorito)
        self.games = sorted(self.games, key=str.lower)
    
    def ficha(self): 
        conteudo = f"[grey93]Nome real:[/] [black on pale_green1 ]{self.nome}[/]"
        conteudo += "\n[grey93]Jogos favoritos:[/]"
        for numeracao, game in enumerate(self.games):
            conteudo += f"\n:joystick: [pale_green3]{game}[/]"
        ficha = Panel(conteudo, title=f"Jogador <{self.nick}>", width= 40, style="dark_sea_green4")
        print(ficha)

j1 = Gamer("Alana Oliveira Pedrosa", "Gangster_malvadeza")
j1.add_favoritos("Life is Strange")
j1.add_favoritos("The Last of Us")
j1.add_favoritos("The Last of Us 2")
j1.add_favoritos("The Walking Dead")
j1.ficha()
