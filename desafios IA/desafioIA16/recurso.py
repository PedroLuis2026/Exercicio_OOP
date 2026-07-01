from abc import ABC, abstractmethod

class Colaborador(ABC):
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario = salario_base

    @abstractmethod
    def calcular_holerite(self):
        pass

class DesenvolvedorJunior(Colaborador):
    inss = 0.075
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)
    
    def calcular_holerite(self):
        salario_t = self.salario - (self.salario * self.inss)
        return salario_t

class DesenvolvedorSenior(Colaborador):
    bonus = 0.15
    imposto = 0.11
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)

    def calcular_holerite(self):
        salario_a = self.salario + (self.salario * self.bonus)
        salario_t = salario_a - (salario_a * self.imposto)
        return salario_t