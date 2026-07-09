from carteira import *

def main():
# 1. Criando uma carteira com saldo positivo
    minha_carteira = Carteira(100.0)
    print(f"Saldo em Reais: [green]R$ {minha_carteira.saldo_reais:.2f}[/]")
    print(f"Saldo em Dólares: [cyan]US$ {minha_carteira.saldo_dolares:.2f}[/]")
    print(f"Saldo em Euros: [yellow]€ {minha_carteira.saldo_euros:.2f}[/]\n")

# 2. Tentando forçar um saldo negativo (O setter deve travar em 0)
    minha_carteira.saldo_reais = -250.0
    print("[bold red]Tentativa de negativar o saldo para -250.0 realizada.[/]")
    print(f"Saldo atual pós-trava: [green]R$ {minha_carteira.saldo_reais:.2f}[/]")

if __name__ == "__main__":
    main()