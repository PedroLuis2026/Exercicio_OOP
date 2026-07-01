from pessoa import Pessoa

class Aluno(Pessoa):#Para fazer uma SubClasse é penas botar parenteses na SubClasse com o nome da Classe Mãe
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)#Sempre que você for fazer o método contrutor na SubClasse, você deve por um super.__init__(parametros da Classe Mãe), para a SubClasse importar os atributos da Classe Mãe
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} fez a matrícula com sucesso!")