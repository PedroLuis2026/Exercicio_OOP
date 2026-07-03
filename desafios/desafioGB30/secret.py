import hashlib
from rich import print
class Credencial:
    def __init__(self):
       self.__hash = None
    
    @property
    def senha(self):
        return self.__hash
    
    @senha.setter
    def senha(self, valor):
        if valor is False or str(valor).strip() == "":
            raise ValueError(f"Na senha deve ser digitado algo")
        else:
            self.__hash = hashlib.sha256(valor.encode('utf-8')).hexdigest()

    def verificar(self, resposta):
        certo = False
        verify = hashlib.sha256(resposta.encode('utf-8')).hexdigest()
        if verify == self.senha:
            certo = True
        else:
            certo = False
        if certo:
            print("Senha confere!")
            print(f"[green]{certo}[/]")
        else:
            print("Senha não bate!")
            print(f"[red]{certo}[/]")
