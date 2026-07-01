from rich import inspect 
from rich import print



class ContaBancaria:
    """
    Conta uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome 
        self.saldo = saldo
    
    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem o saldo de R${self.saldo:.2f}".replace(".", ",")

    def depositar(self):
        while True:
            try:
                saldo = float(input("Digite quanto você quer depositar de saldo: R$ "))
                if saldo <= 0:
                    print("Digite um número maior do que zero!")
                    continue
                self.saldo += saldo  
            except ValueError:
                print("Digite apenas números nessa opção!")
                continue
            return f"Você adicionou R${saldo} a sua conta.".replace(".", ",")

    def retirar(self):
        while True:
            try:
                saldo = float(input("Digite quanto você quer retirar de saldo: R$ "))
                if saldo <= 0:
                    print("Digite um número maior do que zero!")
                    continue
                if saldo > self.saldo:
                    print("Você não possui esse valor para retirada!")
                    continue
                self.saldo -= saldo
            except ValueError:
                print("Digite apenas números nessa opção!")
                continue
            return f"Você retirou R${saldo} da sua conta.".replace(".", ",")


conta1 = ContaBancaria(1203, "Pedro", 5000)

print(conta1)
print(conta1.retirar())
print(conta1)

inspect(conta1)

