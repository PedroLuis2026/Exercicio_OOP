from rich import print

class Cofre:
    def __init__(self):
        self.__senha = "0000"
    
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha: str):
        if len(senha) != 4 or not senha.strip().isdigit():
            raise ValueError("A senha apenas deve possuir 4 números!")
        else:
            self.__senha = senha
    
    def abrir(self, tentativa: str):
        if tentativa == self.__senha:
            print("[green]VOCÊ CONSEGUIU ABRIR O BANCO![/]")
        else:
            print("[red]O ALARME DISPAROU![/]")