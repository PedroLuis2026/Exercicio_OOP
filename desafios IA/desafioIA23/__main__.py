from tokens import *

def main():
    token = TokenAcesso("admin123")

# 1. Errando a senha de propósito 3 vezes para ver o bloqueio permanente
    token.utilizar_token("12345")
    token.utilizar_token("senha_errada")
    token.utilizar_token("admin123") # Aqui zera as tentativas e bloqueia

# 2. Tentando colocar a senha certa APÓS o bloqueio (Deve recusar)
    token.utilizar_token("admin123")
if __name__ == "__main__":
    main()