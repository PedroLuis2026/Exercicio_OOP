from abc import ABC, abstractclassmethod
from rich.panel import Panel
from rich import print


class Funcionario(ABC):
    sal_min = 1612
    inss  = 0.075
    def __init__(self, nome, sal_bruto):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = sal_bruto

    @abstractclassmethod    
    def calc_sal(self):
        pass

    def analisar_sal(self):
        print(Panel(f"O salário de [blue]{self.nome}[/] ([purple4]{self.__class__.__name__}[/]) é de [green]{self.calc_sal()}[/] e corresponde a [orange4]{self.salario / self.sal_min:.1f} salários mínimos[/].", title="Análise de Salário", width=50))

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome, 0)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        sal_b = self.valor_hora * self.horas_trab
        sal_l = sal_b - (sal_b * self.inss)
        self.salario = sal_l
        return f"R${self.salario:.2f}"
    
class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto)
        
    def calc_sal(self):
        sal_l = self.sal_bruto - (self.sal_bruto * self.inss)
        self.salario = sal_l
        return f"R${self.salario:.2f}" 