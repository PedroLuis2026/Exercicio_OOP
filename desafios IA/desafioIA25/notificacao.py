from abc import ABC, abstractmethod
from rich import print
class CanalNotificacao(ABC):
    
    @property
    @abstractmethod
    def destinatario(self):
        pass

    @destinatario.setter
    @abstractmethod
    def destinatario(self, des):
        pass

    @abstractmethod
    def enviar(self, mensagem):
        pass

class NotificacaoEmail(CanalNotificacao):
    def __init__(self, destinata: str):
        self.destinatario = destinata

    @property
    def destinatario(self):
        return self._destinatario
    
    @destinatario.setter
    def destinatario(self, des: str):
        if not des.count("@") == 1 or not des.endswith(".com"):
            raise ValueError("O e-mail do destinatario está errado.")
        self._destinatario = des.strip()

    def enviar(self, mensagem:str):
        print(f"[cyan] E-mail enviado para {self._destinatario}:[/] {mensagem}")

class NotificacaoSMS(CanalNotificacao):
    def __init__(self, destinata: str):
        self.destinatario = destinata
    
    @property
    def destinatario(self):
        return self._destinatario
    
    @destinatario.setter
    def destinatario(self, des:str):
        if len(des) != 13 or not des.isdigit() or not des.startswith("55"):
            raise ValueError("O número do destinatario está errado.")
        self._destinatario = des.strip()
    
    def enviar(self, mensagem:str):
        print(f"[cyan] SMS enviado para o número +{self._destinatario}:[/] {mensagem}")