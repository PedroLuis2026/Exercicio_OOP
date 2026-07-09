from rich import print

class Produto:
    def __init__(self, nome: str, preco: float, categoria: str):
        self.__nome = nome
        self.__preco_base = preco
        self.__categoria = categoria.strip().upper()
        self.preco_base = self.__preco_base
    
    @property
    def preco_base(self):
        return self.__preco_base
    
    @preco_base.setter
    def preco_base(self, preco: float):
        if preco <= 0:
            raise ValueError("O preço não pode ser menor ou igual a zero!")
        self.__preco_base = preco

    @property
    def preco_final(self):
        if self.__categoria == "LIVROS":
            preco_f = self.__preco_base - (self.__preco_base * 0.20)
            return (f"O preço do produto foi ajustado para [green]R$ {preco_f:.2f}[/]".replace(".", ","))
        elif self.__categoria == "ELETRONICOS":
            preco_f = self.__preco_base - (self.__preco_base * 0.10)
            return (f"O preço do produto foi ajustado para [green]R$ {preco_f:.2f}[/]".replace(".", ","))
        else:
            return (f"O preço do produto continua sendo [green]R$ {self.__preco_base:.2f}[/]".replace(".", ","))

    