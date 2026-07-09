from rich import print
class PerfilUsuario:
    def __init__(self, username: str):
        self.__username = username
        self.username = self.__username
    
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, nome: str):
        if  not nome.startswith("@") or " " in nome or len(nome) < 5:
            raise ValueError(f"A senha \"{nome}\" não atende os requesitos necessarios!")
        else:
            self.__username = nome.lower().strip()