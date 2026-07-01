from abc import ABC, abstractmethod
from rich.console import Group
from rich.panel import Panel
from rich import print
class VisualizadorMatriz(ABC):
    def __init__(self, matriz):
        self.matriz = matriz
    
    @abstractmethod
    def desenhar_painel(self):
        pass

class VisualizadorSimples(VisualizadorMatriz):
    def __init__(self, matriz):
        super().__init__(matriz)

    def desenhar_painel(self):
        for i in self.matriz:
            linha = " | ".join(map(str, i))
            print(linha)

class VisualizadorRich(VisualizadorMatriz):
    def __init__(self, matriz):
        super().__init__(matriz)
    
    def desenhar_painel(self):
        linhas_f = []

        for i in self.matriz:
            linha = " | ".join(map(str, i))
            linhas_f.append(linha)
        conteudo = Group(*linhas_f)
        print(Panel(conteudo, title="[bold]- Sala -[/]", border_style="blue", expand=False))             