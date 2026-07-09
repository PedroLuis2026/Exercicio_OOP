from rich import print

class Velocimetro:
    def __init__(self, velocidade: int):
        self.__velocidade_atual = velocidade
        self.__historico = []
        self.velocidade_atual = self.__velocidade_atual
    
    @property
    def velocidade_atual(self):
        return self.__velocidade_atual
    
    @velocidade_atual.setter
    def velocidade_atual(self, definir: int):
        if definir < 0:
            definir = 0
        if definir > 180:
            definir = 180
        self.__velocidade_atual = definir
        self.__historico.append(definir)

    @property
    def historico(self):
        return self.__historico

    @property
    def media_historico(self):
        if len(self.__historico) != 0:
            return sum(self.__historico) / len(self.__historico)
        else:
            return sum(self.__historico)  