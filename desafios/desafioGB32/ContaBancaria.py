import hashlib
import sys
import msvcrt
from rich import print
class ContaBancaria:
    def __init__(self, id, titular: str, saldo: float, senha = None):
        self._id = id
        self._titular = titular.title().strip()
        self.__saldo = saldo
        self.__hash = None
        if senha == None:
            senha = self._pede_senha()
        self.__hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        print(f"Conta de ID[cyan] {self._id}[/] criada com sucesso!")

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novo_nome: str):
        tentativa = hashlib.sha256(self._pede_senha().encode('utf-8')).hexdigest()
        if tentativa != self.__hash:
            print("[red]Senha incorreta!")
            return 
               
        nome_f = novo_nome.title().strip()
        if nome_f == self._titular:
            print("[red]O nome não pode ser o mesmo que o atual![/]")
        else:
            self._titular = nome_f
            print(f"[green]Nome alterado com sucesso para [grey]{self._titular}[/][/].")
                   


    def _pede_senha(self) -> str:
        print("Digite a senha: ", end="", flush=True)
        senha = ""
        while True:
            cr = msvcrt.getch()
            if cr in (b'\r', b'\n'):
                print()
                break
            elif cr == b'\x08':
                if len(senha) > 0:
                    senha = senha[:-1]
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
            else:
                try:
                    caractere = cr.decode('utf-8')
                    senha += caractere
                    sys.stdout.write('*')
                    sys.stdout.flush()
                except UnicodeDecodeError:
                    print("[red]Erro[/]")
        return senha

    @property
    def saldo(self):
        return f"O saldo atual da conta é de [green]R$ {self.__saldo:,.2f}[/]."

    def depositar(self, valor: float):
        if valor <= 0:
            print("[red]O valor não pode ser menor ou igual a zero![/]")
        else:
            self.__saldo += valor
            print(f"O saldo atual da conta de [gold1]{self._titular}[/], agora é de [green]R$ {self.__saldo:,.2f}[/].")
        
    def sacar(self, valor: float):
        tentativa = hashlib.sha256(self._pede_senha().encode('utf-8')).hexdigest()
        if tentativa != self.__hash:
            print("[red]Senha incorreta![/]") 
        else:
            if valor <= 0:
                print("[red]O valor do saque deve ser maior que zero![/]")
            elif valor > self.__saldo:
                print("[red]Saldo insuficiente para realizar o saque![/]")
            else:
                self.__saldo -= valor
                print(f"O saldo atual da conta de [gold1]{self._titular}[/], agora é de [green]R$ {self.__saldo:,.2f}[/].")

    def validar_senha(self, chave: str) -> bool:
        chave = hashlib.sha256(chave.encode('utf-8')).hexdigest()
        if chave != self.__hash:
            print("[red]Senha incorreta![/]")
        else:
            print("[green]Senha correta![/]")