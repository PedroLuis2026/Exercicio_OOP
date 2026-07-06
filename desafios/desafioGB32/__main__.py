from ContaBancaria import *
from rich import print, inspect
def main():
    print("Criando conta[yellow]...[/]")
    cc = ContaBancaria(123, "Alana", 2300, "Luis")
    cc.sacar(1000)
    inspect(cc, private=True, methods=True)
if __name__ == "__main__":
    main()