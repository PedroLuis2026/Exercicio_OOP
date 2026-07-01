import os
os.system("cls" if os.name == "nt" else "clear")
from rich import print
from time import sleep

class Livro:

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f"[blue]:open_book: Você acabou de abrir o livro \"[red3]{self.titulo}[/]\" que tem [dark_sea_green]{paginas} páginas[/] no total. Você agora está na [light_goldenrod3]página {self.pagina_atual}[/][/]")
    
    def avancar_paginas(self, passar):
        contador = 0
        for i in range (0, passar, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} ", end="-> ")
                sleep(1)
                contador += 1
        print(f"[blue]Você avançou {contador} páginas e agora está na [light_goldenrod3]página {self.pagina_atual}[/]")
        if self.fim_do_livro():
            print(f":rotating_light:[red] Você chegou ao final do livro \"{self.titulo}\"")
                

    def fim_do_livro(self):    
        return True if self.pagina_atual == self.paginas else False

l1 = Livro("Os contos do meu primeiro amor", 20)
l1.avancar_paginas(4)
l1.avancar_paginas(10)
l1.avancar_paginas(100)

