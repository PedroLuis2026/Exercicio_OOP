import os 
from rich import print
from rich.panel import Panel
os.system("cls" if os.name == "nt" else "clear")

class Temperatura:
    def __init__(self, id_sensor= "0000" , temp_atual= 0.0):
        self.id_sensor = id_sensor
        self.temp_atual = temp_atual
    
    def atualizar_temp(self,nova_temp):
        if nova_temp < 20:
            cor = "navy_blue"
        elif 20 <= nova_temp <= 25:
            cor = "dark_sea_green"
        else:
            cor = "bold red1"
        self.temp_atual = nova_temp
        print(Panel(f"A nova temperatura foi definida em [{cor}]{nova_temp}°[/]",style="grey69", border_style="honeydew2",expand=False))
    
    def status(self):
        if self.temp_atual < 20:
            cor = "navy_blue"
            print(Panel(f"[bold]TEMPERATURA ATUAL:[/][{cor}]{self.temp_atual}°[/]\n"
                        f"[{cor}]RESFRIAMENTO OTIMIZADO.[/]",title=f"[{cor}]- {self.id_sensor} -[/]",border_style=f"{cor}", style="grey69", expand=False))
        elif 20 <= self.temp_atual <= 25:
             cor = "dark_sea_green"
             print(Panel(f"[bold]TEMPERATURA ATUAL:[/][{cor}]{self.temp_atual}[/]\n"
                        f"[{cor}]TEMPERATURA ESTÁVEL.[/]",title=f"[{cor}]- {self.id_sensor} -[/]",border_style=f"{cor}", style="grey69", expand=False))
        else:
            cor = "bold red1"
            print(Panel(f"[bold]TEMPERATURA ATUAL:[/][{cor}]{self.temp_atual}[/]\n"
                        f"[blink {cor}]:warning: ALERTA: SUPERAQUECIMENTO[/]",title=f"[{cor}]- {self.id_sensor} -[/]",border_style=f"{cor}", style="grey69", expand=False))

s1 = Temperatura("Rack-01", 22.5)
s1.atualizar_temp(19)
s1.status()