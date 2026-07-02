from diario import *
from rich import print, inspect

def main():
    d = Diario("Doidera")

    d.escrever("Massa dms")
    d.escrever("Assina o contrato")
    d.escrever("Faculdade massa")

    d.ler("Doidera")

    inspect(d, private=True, methods=True)
if __name__ == "__main__":
    main()