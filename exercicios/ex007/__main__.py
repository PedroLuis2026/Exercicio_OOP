from rich import inspect
from classesex005 import Aluno, Professor, Funcionario

def main():
    a1 = Aluno("Pedro", 19, "ADS", "Matiurna")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    a1.estudar
    inspect(a1, methods=True)

    p1 = Professor("Guanabara", 47, "TI", "Mestre")
    p1.fazer_aniversario()
    p1.dar_aula()
    p1.estudar()
    inspect(p1, methods=True)

    f1 = Funcionario("Murilo", 45, "Gerente", "RH")
    f1.fazer_aniversario()
    f1.bater_ponto()
    f1.estudar()
    inspect(f1, methods=True)

if __name__ == "__main__":
    main()