from cofre import *

def main():
    cofre = Cofre()

# 1. Tentando definir uma senha inválida (Vai disparar o ValueError)
    try:
        cofre.senha = "12a4"
    except ValueError as e:
        print(f"[bold yellow]Validação funcionando:[/] {e}")

# 2. Definindo uma senha válida
    cofre.senha = "9876"

# 3. Testando o método abrir
    cofre.abrir("0000")  # Saída: O ALARME DISPAROU!
    cofre.abrir("9876")  # Saída: VOCÊ CONSEGUIU ABRIR O BANCO!

if __name__ == "__main__":
    main()