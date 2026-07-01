from abc import ABC, abstractmethod

class CriaturaParanormal(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    @abstractmethod
    def manifestar_presenca(self):
        pass

class CriaturaSangue(CriaturaParanormal):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def manifestar_presenca(self):
        print("Manifestou uma aura de violência e dor física!")

class CriaturaConhecimento(CriaturaParanormal):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
    
    def manifestar_presenca(self):
        print("Sussurrou verdades perturbadoras na mente dos investigadores!")
