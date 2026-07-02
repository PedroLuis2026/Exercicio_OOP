import hashlib

class Credencial:
    def __init__(self):
        self.__hassh = hashlib.sha256("asçdf]~gdçf".encode('utf-8')).hexdigest()
        self.senha = self.__hassh
    @property
    def senha(self):
        return self.senha
    
    def validar(self):
        pass
    