import os
os.system("cls" if os.name == "nt" else "clear")
from treino import * 

def main():
    p1 = TreinoHip()
    p1.executar_rotina()

    p2 = TreinoCar()
    p2.executar_rotina()

if __name__ == "__main__":
    main()