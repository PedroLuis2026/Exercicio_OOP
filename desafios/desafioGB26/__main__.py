from funcionarios import *
import os
os.system("cls" if os.name == "nt" else "clear")

def main():
    f1 = FuncionarioHorista("Paulo", 12, 200)
    f1.calc_sal()
    f1.analisar_sal()

    f2 = FuncionarioMensalista("Amanda", 9500)
    f2.calc_sal()
    f2.analisar_sal()

if __name__ == "__main__":
    main()