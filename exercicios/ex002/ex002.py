#Declaração de classe
class gafanhoto:
    """
Essa classe cria um Gafanhoto, que é uma pessoa que possui nome e idade.

Para criar uma nova pessoa, use:
Variavel = Gafanhoto(nome, idade)

E possui métodos para modificar os atributos do objeto:
Variavel.aniversario() aumenta em +1 o atributo de idade
Variavel.mensagem() retorna uma string que possui o atributo de nome e idade da variavel
    """
    def __init__(self, nome = "vazio", idade = 0): #Método contrutor
        #atributo de instância
        self.nome = nome
        self.idade = idade
    #Métodos de instâncias
    def aniversario(self):
        self.idade += 1

    def __str__(self): #Dunder method
        return f"{self.nome} é um Gafanhoto, e tem {self.idade} anos de idade."

#Declaração de objetos
g1 = gafanhoto("Pedro", 19)
g1.aniversario()
print(g1)

g2 = gafanhoto("Juliana", 40)
g2.aniversario()
print(g2)

g3 = gafanhoto()
print(g3)

print(gafanhoto().__doc__)