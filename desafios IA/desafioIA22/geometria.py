
class Triangulo:
    def __init__(self, ladoa:int, ladob:int, ladoc:int):
        self._lado_a = ladoa
        self._lado_b = ladob
        self._lado_c = ladoc
        self.lados = (self._lado_a, self._lado_b, self._lado_c)
    
    @property
    def lados(self):
        return (self._lado_a, self._lado_b, self._lado_c)

    @lados.setter 
    def lados(self, lados:tuple):
        if lados[0] + lados[1] <= lados[2] or lados[1] + lados[2] <= lados[0] or lados[2] + lados[0] <= lados[1]:
            raise ValueError("Os lados não formam um triângulo!")
        else:
            self._lado_a = lados[0]
            self._lado_b = lados[1]
            self._lado_c = lados[2]
            print("Os lados foram modificados, e formam um triângulo.")