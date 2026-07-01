from abc import ABC, abstractclassmethod
from rich.panel import Panel 
from rich import print
from rich.console import Group 


class BebidaQuente(ABC):
    def preparar(self):
        conteudo = Group(self.ferver_agua(), self.misturar(), self.servir())
        
        print(Panel(conteudo,title="--- Servindo Bebida ---", subtitle="--- Bebida Pronta ---", border_style="orange4"))
    
    def ferver_agua(self):
        return "1. Fervendo água a 100 graus Celcius.\n"
    
    @abstractclassmethod
    def misturar(self):
        pass

    @abstractclassmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):

    def misturar(self):
        return "2. Passando água pressurizada pelo pó de café moído.\n"
    
    def servir(self):
        return "3. Servindo em xícara pequena."

class Cha(BebidaQuente):

    def misturar(self):
        return "2. Mergulhando o sachê de ervas na água.\n"

    def servir(self):
        return "3. Servindo na caneca de porcelana com limão."

class Leite(BebidaQuente):

    def misturar(self):
        return "2. Passando vapor pressurizando pelo bico do leite.\n"
    
    def servir(self):
        return "3. Servindo na caneca grande, já com leite."