from abc import ABC, abstractclassmethod

class Transporte(ABC):
    def __init__(self, distancia, frete):
        self.distancia = distancia
        self.frete = frete

    @abstractclassmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    fator = 0.50
    def __init__(self, distancia, frete=0):
        super().__init__(distancia, frete)
        self.distancia = distancia
        self.frete = self.fator
    
    def calc_frete(self):
        valor = self.distancia * self.frete
        return f"R$[light_sky_blue1]{valor:.2f}"

class Caminhao(Transporte):
    fator = 1.20
    def __init__(self, distancia, frete=0):
        super().__init__(distancia,frete)
        self.distancia = distancia
        self.frete = self.fator
    
    def calc_frete(self):
        valor = self.distancia * self.frete
        return f"R$[light_sky_blue1]{valor:.2f}" if self.distancia >= 50 else "Raio mínimo de [red1]50km[/]"

class Drone(Transporte):
    fator = 9.50
    def __init__(self, distancia, frete=0):
        super().__init__(distancia,frete)
        self.distancia = distancia  
        self.frete = self.fator
    
    def calc_frete(self):
        valor = self.distancia * self.frete
        return f"R$[light_sky_blue1]{valor:.2f}" if 0 < self.distancia <= 10 else "Raio máxino de [red]10km[/]"
