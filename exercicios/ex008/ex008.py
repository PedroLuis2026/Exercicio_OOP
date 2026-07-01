class ContaBancaria:
    """
    Conta uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id # publico(+)
        self._titular = nome # protegido(#)
        self.__saldo = saldo # privado(-)
        print(f"Conta {self.id} foi cirada com sucesso. Saldo atual de R${self.__saldo:,.2f}")
    def __str__(self):
        #return f"A conta {self.id} de {self._titular} tem o saldo de R${self.saldo:.2f}".replace(".", ",")
        return f"Estado atual da conta: {self.__dict__}"

    def depositar(self, din):
        din = abs(din)
        self.__saldo += din
        f_din = f"{din:.2f}".replace(".", ",")
        print(f"Você adicionou R${f_din} na conta {self.id}.")
    def retirar(self, din):
        din = abs(din)
        self.__saldo -= din
        f_din = f"{din:.2f}".replace(".", ",")
        print(f"Você retirou R${f_din} da sua conta {self.id}.")
