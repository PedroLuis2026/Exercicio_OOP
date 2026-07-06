from abc import abstractmethod, ABC
from rich import print
from random import choice
class Pessoa(ABC):
    def __init__(self, nome: str, nascimento: int):
        self._nome = nome.title().strip()
        self._nascimento = 0
        self.nascimento = nascimento
    
    @property
    @abstractmethod
    def nome(self):
        pass

    @property
    @abstractmethod
    def nascimento(self):
        pass
    
    @nascimento.setter
    @abstractmethod
    def nascimento(self, n_nascimento:int ):
        pass

    @property
    @abstractmethod
    def idade(self):
       pass
    
class Aluno(Pessoa):
    def __init__(self, nome: str, nascimento: int, curso = None):
        super().__init__(nome, nascimento)
        self.cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]
        if curso == None:
            curso = choice(self.cursos_oficiais)
        self._curso = None
        self.curso = curso
        
    @property
    def nome(self):
        return self._nome

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, n_nascimento: int):
        if n_nascimento == self._nascimento:
            print("[red]O novo nascimento não pode ser igual ao antigo![/]")
            return 
        elif n_nascimento > 2026 or n_nascimento < 1970:
            raise ValueError(f"Ano {n_nascimento} é inválido.")
        else:
            self._nascimento = n_nascimento
            print(f"[green]A data de nascimento foi atualizada para {self._nascimento}[/].")

    @property
    def idade(self):
        return 2026 - self._nascimento

    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, curso: str):
        curso_f = curso.strip().upper()
        if curso not in self.cursos_oficiais:
            raise ValueError(f"O curso {curso} não está na lista de cursos oficiais.")
        else:
            self._curso = curso

    def add_curso(self, curso: str):
        curso_f = curso.strip().upper()
        if curso in self.cursos_oficiais:
            print("[yellow]O curso já está dentro na listagem dos cursos oficiais.[/]") 
        else:
            self.cursos_oficiais.append(curso)