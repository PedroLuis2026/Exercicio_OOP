from rich import print

class Carteira:
    def __init__(self, saldo: float):
        self._saldo_reais = saldo
        self.saldo_reais = self._saldo_reais

    @property
    def saldo_dolares(self):
        dolar = self._saldo_reais * 0.19
        return dolar

    @property
    def saldo_euros(self):
        euro = self._saldo_reais * 0.17
        return euro
    
    @property
    def saldo_reais(self):
        return self._saldo_reais

    @saldo_reais.setter
    def saldo_reais(self, valor: float):
        if valor < 0:
            self._saldo_reais = 0
        else:
            self._saldo_reais = valor