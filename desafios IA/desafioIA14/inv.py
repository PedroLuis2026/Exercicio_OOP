from abc import ABC, abstractmethod
from rich import print
from random import randint

class Arma(ABC):
    def __init__(self, nome, dano_base):
        self.nome = nome
        self.dano_base = dano_base

    @abstractmethod
    def atacar(self):
        pass

class ArmaCorpoCorpo(Arma):
    forca = 3
    def __init__(self, nome, dano_base):
        super().__init__(nome, dano_base)
    
    def atacar(self, alvo):
        dano_t = self.dano_base + self.forca
        print(f"O [blue]{alvo}[/] recebe [red]{dano_t}[/]")

class ArmaFogo(Arma):
    def __init__(self, nome, dano_base, municao):
        super().__init__(nome, dano_base)
        self.municao = municao
    
    def atacar(self, alvo):
        if self.municao > 0:
            self.municao -= 1
            tiro = randint(1, 8)
            dano_t = self.dano_base + tiro
            print(f"O [blue]{alvo}[/] recebe [red]{dano_t}[/]")
        else:
            print(f"[red1]A arma está descarregada.[/]")

    