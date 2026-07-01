import os 
os.system("cls" if os.name == "nt" else "clear")
from cafeteira import *

def main():
    bebida = Cafe()
    bebida.preparar()

if __name__ == "__main__":
    main() 