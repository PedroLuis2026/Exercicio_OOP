from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class CartaoPassagem(ABC):
    def __init__(self, id_cartao, saldo):
        self.id_cartao = id_cartao
        self.saldo = saldo

    def recarregar(self, valor):
        self.saldo += valor
    
    @abstractmethod
    def descontar_viagem(self):
        pass

class CartaoEstudante(CartaoPassagem):
    def __init__(self, id_cartao, saldo):
        super().__init__(id_cartao, saldo)
    
    def descontar_viagem(self):
        passagem = 2.55
        self.saldo -= passagem
        if self.saldo <= 0:
            self.saldo = 0
            print(Panel("SALDO INSUFICIENTE",border_style="red1", style="red", title="SALDO INSUFICIENTE"))
        else:
            print(f"Foi descontado R${passagem} do seu saldo do VEM, o seu saldo atual é R${self.saldo:.2f}".replace(".", ","))
 

class CartaoComum(CartaoPassagem):
    def __init__(self, id_cartao, saldo):
        super().__init__(id_cartao, saldo)
    
    def descontar_viagem(self):
        passagem = 5.10
        self.saldo -= passagem
        if self.saldo <= 0:
            self.saldo = 0
            print(Panel("SALDO INSUFICIENTE",border_style="red1", style="red", title="SALDO INSUFICIENTE"))
        else:
            print(f"Foi descontado R${passagem} do seu saldo do VEM, o seu saldo atual é R${self.saldo:.2f}".replace(".", ","))
