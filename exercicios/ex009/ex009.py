class Avaliacao:
    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disp = disciplina
        self._nota = nota

    def set_nota(self, valor):
        if 0 <= valor <= 10:
            return self._nota
        else:
            print("Nota inválida!")
    def get_nota(self):
        return self._nota