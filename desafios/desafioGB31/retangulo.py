from rich import print
class Retangulo:
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura
        self._area = None
    
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, valor):
        if valor < 0:
            raise ValueError("Valor inválido para base")
        else:
            self._base = valor
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, valor):
        if valor < 0:
            raise ValueError("Valor inválido para altura")
        else:
            self._altura = valor
    
    @property
    def area(self):
        self._area = self.altura * self.base
        return self._area
    
    @property
    def medidas(self):
        return self.medidas
    
    @property
    def medidas(self):
        return f"Base = [cyan]{self.base}[/]\nAltura = [cyan]{self.altura}[/]\nÁrea = [cyan]{self.area}[/]"
    
    @medidas.setter
    def medidas(self, valores):
        if isinstance(valores,(tuple, list)) and len(valores) == 2:
            self.base = valores[0]
            self.altura = valores[1]
        else:
            raise ValueError("Digite duas númerações dentro da tupla, exemplo: (Base, Altura)")
        
    