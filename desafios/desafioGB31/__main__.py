from retangulo import *
from rich import print, inspect
def main():
    r = Retangulo(8, 4)

    r.base = 23

    inspect(r, private=True, methods=True)
if __name__ == "__main__":
    main()