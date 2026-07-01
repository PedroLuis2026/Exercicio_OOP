from abc import ABC, abstractclassmethod
from rich import print
import math

class Poligono(ABC):
    def __init__(self, lados):
        self.qtd_lados = lados

    @abstractclassmethod
    def perimetro():
        pass

    @abstractclassmethod
    def area():
        pass

class Quadrado(Poligono):
    def __init__(self, lado=1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        perimetro = self.lado * 4
        return f"[pale_turquoise1]{perimetro:.1f}[/]"

    def area(self):
        area = self.lado**2
        return f"[pale_turquoise1]{area:.2f}[/]"

class Circulo(Poligono):
    def __init__(self, raio=1):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        perimetro = 2 * math.pi * self.raio
        return f"[pale_turquoise1]{perimetro:.2f}[/]"

    def area(self):
        area = math.pi * self.raio**2
        return f"[pale_turquoise1]{area:.2f}[/]"

class Triangulo(Poligono):
    def __init__(self, lado=2, base=3, altura=3):
        super().__init__(3)
        self.lado = lado
        self.base = base
        self.altura = altura

    def perimetro(self):
        perimetro = self.lado * 3
        return f"[pale_turquoise1]{perimetro:.2f}[/]"

    def area(self):
        area = self.base * self.altura / 2
        return f"[pale_turquoise1]{area:.2f}[/]"

