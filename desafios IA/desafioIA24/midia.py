from abc import ABC, abstractmethod

class Midia(ABC):
    def __init__(self, titulo: str, ano_p: int):
        self.titulo = titulo
        self.ano_publicacao = ano_p
    
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, novo_t: str):
        if novo_t == "":
            raise ValueError("O novo título não pode não conter nada.")
        novo_tf = novo_t.strip().title().replace(" De ", " de ").replace(" Da ", " da ").replace(" Do ", " do ")
        self._titulo = novo_tf

    @property
    def ano_publicacao(self):
        return self._ano_publicacao

    @ano_publicacao.setter
    def ano_publicacao(self, novo_an: int):
        if novo_an <= 0 or novo_an > 2026:
            raise ValueError("O novo ano não pode ser maior que o ano atual.")
        self._ano_publicacao = novo_an

    @property 
    @abstractmethod
    def obter_tipo(self):
        pass

class Livro(Midia):
    def __init__(self, titulo, ano_p, num_pag: int):
        super().__init__(titulo, ano_p)
        self.num_pag = num_pag
    
    @property
    def num_pag(self):
        return self._num_pag

    @num_pag.setter
    def num_pag(self, num_pagn: int):
        if num_pagn < 1:
            raise ValueError("Você não pode passar zero páginas ou páginas negativas.")
        self._num_pag = num_pagn
    
    @property 
    def obter_tipo(self):
        return "Livro"

class VideoAula(Midia):
    def __init__(self, titulo, ano_p, duracao_seg: int):
        super().__init__(titulo, ano_p)
        self.duracao = duracao_seg
    
    @property
    def duracao(self):
        return self._duracao
    
    @duracao.setter
    def duracao(self, duracao_segn: int):
        if duracao_segn <= 0:
            raise ValueError("O vídeo não pode conter zero segundos ou menos.")
        self._duracao = duracao_segn
    
    @property
    def obter_tipo(self):
        return "Vídeo"