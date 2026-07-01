from matriz import *
import os
os.system("cls" if os.name == "nt" else "clear")

def main():
    # --- ÁREA DE TESTES (Exemplo de uma matriz/mapa de RPG) ---

# Representação de um mapa ou dados (0 = Vazio, 1 = Parede, 2 = Monstro)
    mapa_sala = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 2, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]

    # Criando as instâncias dos visualizadores com a mesma matriz
    vis_simples = VisualizadorSimples(mapa_sala)
    vis_rich = VisualizadorRich(mapa_sala)

    # Executando os painéis
    vis_simples.desenhar_painel()
    vis_rich.desenhar_painel()

if __name__ == "__main__":
    main()