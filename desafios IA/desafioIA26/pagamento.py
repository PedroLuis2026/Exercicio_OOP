from abc import ABC, abstractmethod
from rich import print

class MetodoPagamento(ABC):
    
    @property
    @abstractmethod
    def taxa_servico(self):
        pass

    @taxa_servico.setter
    @abstractmethod
    def taxa_servico(self, valor):
        pass

    @abstractmethod
    def processar(self, valor): 
        pass

class PagamentoPix(MetodoPagamento):
    def __init__(self):
        self.taxa_servico = 0
    
    @property
    def taxa_servico(self):
        return self.__taxa_servico
    
    @taxa_servico.setter
    def taxa_servico(self, valor:float):
        if valor < 0:
            raise ValueError("O valor não pode ser menor do que zero.")
        self.__taxa_servico = valor

    def processar(self, valor:float):
        if valor <= 0:
            raise ValueError("O valor de pagamento não pode ser menor ou igual a zero.")
        else:
            taxa = valor + (valor * (self.__taxa_servico / 100)) if self.__taxa_servico > 0 else valor
            print(f"Você deverá pagar [green]R$ {taxa:.2f}[/].".replace(".", ","))
        
class PagamentoCartao(MetodoPagamento):
    def __init__(self):
        self.taxa_servico = 5

    @property
    def taxa_servico(self):
        return self.__taxa_servico
    
    @taxa_servico.setter
    def taxa_servico(self, valor:float):
        if valor < 0:
            raise ValueError("O valor não pode ser menor do que zero.")
        self.__taxa_servico = valor

    def processar(self, valor:float):
        if valor <= 0:
            raise ValueError("O valor de pagamento não pode ser menor ou igual a zero.")
        else:
            taxa = valor + (valor * (self.__taxa_servico / 100)) if self.__taxa_servico > 0 else valor
            print(f"Você deverá pagar [green]R$ {taxa:.2f}[/].".replace(".", ","))