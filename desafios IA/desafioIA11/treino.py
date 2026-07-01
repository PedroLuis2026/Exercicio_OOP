from abc import ABC, abstractmethod

class Treino(ABC):
    @abstractmethod
    def executar_rotina(self):
        pass

class TreinoHip(Treino):
    def executar_rotina(self):
        print("Aquecimento + 4 séries até a falha com carga máxima.")

class TreinoCar(Treino):
    def executar_rotina(self):
        print("30 minutos em ritmo moderado na esteira ou simulador de escada.")

