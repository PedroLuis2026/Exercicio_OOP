from poligonos import *
import os
os.system("cls" if os.name == "nt" else "clear")

def main():
    q1 = Quadrado(10)
    print(f"O quadrado de lado [pale_turquoise1]{q1.lado}cm[/] tem um perímetro de {q1.perimetro()}cm².")
    print(f"O quadrado de lado [pale_turquoise1]{q1.lado}cm[/] tem uma área de {q1.area()}cm².")

    c1 = Circulo(5)
    print(f"O círculo de raio [pale_turquoise1]{c1.raio}cm[/] tem um perímetro de {c1.perimetro()}cm².")
    print(f"O círculo de raio [pale_turquoise1]{c1.raio}cm[/] tem uma área de {c1.area()}cm².")

    t1 = Triangulo(5, 5, 5)
    print(f"O triângulo de lado [pale_turquoise1]{t1.lado}cm[/] tem um perímetro de {t1.perimetro()}cm².")
    print(f"O triângulo de lado [pale_turquoise1]{t1.lado}cm[/] tem uma área de {t1.area()}cm².")
    

if __name__ == "__main__":
    main()