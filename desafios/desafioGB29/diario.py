from rich import print

class Diario:
    def __init__(self, senha = "pdasjg"):
        self.__segredos = []
        self.__senha = senha

    def escrever(self, escrita):
        self.__segredos.append(escrita)
    
    @property
    def senha(self):
        return self.__senha

    def ler(self,senha):
        if senha != self.__senha:
            raise PermissionError("Senha inválida! Você não pode ler esse diário!")
        else:
            print("[green]Diário LIBERADO![/]")
            for i, v in enumerate(self.__segredos):
                print(f"- {v}")