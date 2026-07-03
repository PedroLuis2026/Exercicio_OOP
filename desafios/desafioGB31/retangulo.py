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
        self._base = valor
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, valor):
        self._altura = valor
    
    @property
    def area(self):
        self._area = self.altura * self.base
        return self._area
    
    @area.setter
    def area(self, valor):
        self._area = valor
    
    