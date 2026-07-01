from rich import inspect

class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade
    
    def fazer_aniversario(self):
        self.idade += 1 


class Aluno(Pessoa):#Para fazer uma SubClasse é penas botar parenteses na SubClasse com o nome da Classe Mãe
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)#Sempre que você for fazer o método contrutor na SubClasse, você deve por um super.__init__(parametros da Classe Mãe), para a SubClasse importar os atributos da Classe Mãe
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} fez a matrícula com sucesso!")

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
    
    def dar_aula(self):
        print(f"Prof. {self.nome} começou a dar aula!")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
    
    def bater_ponto(self):
        print(f"{self.nome} acabou de bater o seu ponto!")

a1 = Aluno("Pedro", 19, "ADS", "Matiurna")
a1.fazer_aniversario()
a1.fazer_matricula()
inspect(a1, methods=True)

p1 = Professor("Guanabara", 47, "TI", "Mestre")
p1.fazer_aniversario()
p1.dar_aula()
inspect(p1, methods=True)

f1 = Funcionario("Murilo", 45, "Gerente", "RH")
f1.fazer_aniversario()
f1.bater_ponto()
inspect(f1, methods=True)