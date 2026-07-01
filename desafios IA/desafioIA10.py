import os
from rich import print
from rich.panel import Panel
from rich.console import Group
from rich.console import Console
from time import sleep
os.system("cls" if os.name == "nt" else "clear")
console = Console()
class LogSistema:
    def __init__(self, nivel="INFO", mensagem=""):
        self.nivel = nivel.upper()
        self.mensagem = mensagem
    
    def sistema(self):
        config={
            'INFO': {'cor': "bold white on blue", 'emoji': ":information:"},
            'ERRO': {'cor': "bold white on red", 'emoji': ":warning :"},
            'FATAL': {'cor': "bold white on red1", 'emoji': ":warning:"}
        }
        dados = config.get(self.nivel, {'cor': "white", 'emoji': ":question:"})
    
        console.log(
            f"[{dados['cor']}] {dados['emoji']} {self.nivel} [/] {self.mensagem}"
        )

l1 = LogSistema("info", "Você abriu o VSCODE")
l1.sistema()
sleep(1)

l2 = LogSistema("erro", "Não consegui achar o Banco de Dados")
l2.sistema()
sleep(1)

l3 = LogSistema("fatal", "O seu aparelho está sobreaquecendo!!!")
l3.sistema()
sleep(1)