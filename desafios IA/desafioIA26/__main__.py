from pagamento import *

def main():
# Instanciando as classes filhas
    pix = PagamentoPix()
    cartao = PagamentoCartao()

    print("[bold cyan]=== TESTANDO PAGAMENTOS ===[/]")

# Compra de R$ 100,00 no Pix (taxa 0% -> deve dar R$ 100,00)
    pix.processar(100.00)

# Compra de R$ 100,00 no Cartão (taxa 5% -> deve dar R$ 105,00)
    cartao.processar(100.00)

    print("\n[bold yellow]=== TESTANDO VALIDAÇÕES ===[/]")
    try:
        pix.processar(-50) # Deve barrar o valor inválido
    except ValueError as e:
        print(f"[red]Erro esperado:[/] {e}")
if __name__ == "__main__":
    main()