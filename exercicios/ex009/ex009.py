class Avaliacao:
    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disp = disciplina
        self._nota = nota

#Métodos Acessores

    def set_nota(self, valor): #Método setter(Módifica a nota em qualquer lugar, mesmo ele não sendo um local permitido)
        if 0 <= valor <= 10:
            self._nota = valor
            return self._nota
        else:
            print("Nota inválida!")
    def get_nota(self): #Método getter(Acessa os dados dentro do atributo protegida)
        return self._nota