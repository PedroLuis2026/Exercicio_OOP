class Termostato:
    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor > 30:
            valor = 30
        if valor < 16:
            valor = 16
        if valor % 0.5 != 0:
            raise ValueError(f"A temperatura {valor}°C é inválida.")
        else:
            self.__temperatura = valor
            return f"A temperatura foi alterada para{self.__temperatura}°C"
    
    @property
    def ftemperatura(self):
        return f"{self.__temperatura}°C"
    


            
    
