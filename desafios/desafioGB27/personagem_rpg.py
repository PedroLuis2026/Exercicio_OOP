from abc import ABC, abstractclassmethod
from random import choice, randint
from rich import print
class Personagem(ABC):
    golpes_g = ["Soco", "Facada", "Pulo Giratório", "Mortal Carpado"]
    golpes_m = ["Bola de fogo", "Bola de Gelo", "Inferno", "Eloquência"]
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self, alvo, força):
        print(f"[green]{self.nome}[/]([blue]{self.vida}[/]) atacou [red]{alvo.nome}[/]([blue]{alvo.vida}[/]) com um [blue]{choice(self.golpes_g) if self.__class__.__name__ == "Guerreiro" else choice(self.golpes_m)}[/] de força {força}")
        print(alvo.receber_dano(força))

    def receber_dano(self, dano):
        metade = dano -(dano * 0.50)
        fator = randint(int(metade),dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        return f"[blue]{self.nome}[/] recebeu [red]dano de {fator}[/]!"
    
    @abstractclassmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init(self, nome, vida):
        super().__init__(nome,vida)

    def curar(self):
        print(f"[blue]{self.nome}[/] enrolou uma [green1]atadura[/] nos ferimentos e [green]recuperou {randint(1, 20)} pontos[/] de vida.")



class Mago(Personagem):
    def __init(self, nome, vida):
        super().__init__(nome,vida)

    def curar(self):
        print(f"[blue]{self.nome}[/] usou uma [green1]magia de cura[/] e [green]recuperou {randint(10,100)} pontos[/] de vida.")
    
    
