#Declaração de classe
class gafanhoto:
    def __init__(self): #Método contrutor
        #atributo de instância
        self.nome = ""
        self.idade = 0
    #Métodos de instâncias
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é garfanhoto e tem {self.idade} anos de idade."

#Declaração de objetos
g1 = gafanhoto()
g1.nome = "Pedro"
g1.idade = 19
g1.aniversario()
print(g1.mensagem())

g2 = gafanhoto()
g2.nome = "Juliana"
g2.idade = 40
g2.aniversario()
print(g2.mensagem())