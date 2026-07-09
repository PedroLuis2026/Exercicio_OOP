from hashlib import *
from rich import print

class TokenAcesso:
    def __init__(self, chave:str):
        self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        self.__tentativas_restantes = 3
        
    
    @property
    def chave(self):
        return self.__hash

    @chave.setter
    def chave(self, n_chave:str):
        if n_chave == "":
            raise ValueError("A nova chave tem que conter no mínimo uma caractere!")
        n_chave = sha256(n_chave.encode('utf-8')).hexdigest()
        self.__hash = n_chave

    def utilizar_token(self, chave_teste:str):
        if self.__tentativas_restantes == 0:
            print("[red]Token esgotado.[/]")
        else:
            if chave_teste == "":
                raise ValueError("A senha deve conter no mínimo uma caractere!")
            chave_teste = sha256(chave_teste.encode('utf-8')).hexdigest()
            if chave_teste == self.__hash:
                print("[green]Token liberado.[/]")
            else:
                self.__tentativas_restantes -= 1
                print("[red]Senha inválida para o token.[/]")