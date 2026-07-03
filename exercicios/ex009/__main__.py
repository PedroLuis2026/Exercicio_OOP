from ex009 import *

def main():
    av1 = Avaliacao("Alana", "Português", 8.5)
    av1.set_nota(7.4)
    print(f"{av1.nome} tirou {av1.get_nota()} em {av1.disp}")
if __name__ == "__main__":
    main()
    