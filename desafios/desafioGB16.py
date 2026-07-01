import os
from rich import print




os.system("cls" if os.name == "nt" else "clear")

class Funcionarios:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentação(self):
        return f":handshake: Olá, meu nome é [bright_blue]{self.nome}[/] e sou [bright_yellow]{self.cargo}[/] do setor de [grey37]{self.setor}[/] da empresa Gueguelesca."

c1 = Funcionarios("Pedro", "TI", "Senior")
print(c1.apresentação())