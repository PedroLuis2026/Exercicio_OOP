from secret import *
from rich import print, inspect
def main():
    c = Credencial()
    c.senha = "asdf"

    c.verificar("asdf")
    inspect(c, methods=True, private=True)
if __name__ == "__main__":
    main()
    