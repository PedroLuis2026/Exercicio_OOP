from perfil import *

def main():
# Cenário 1: Tudo certo (Salva em minúsculo com sucesso)
    usuario1 = PerfilUsuario("@LuisPaulo")
    print(f"Username criado: [green]{usuario1.username}[/]\n")

# Cenário 2: Forçando o erro (O Python vai travar o programa antes de salvar o dado podre)
    usuario2 = PerfilUsuario("luis")

if __name__ == "__main__":
    main()