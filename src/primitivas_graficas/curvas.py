from src.primitivas_graficas import Rasterizacao, Bresenham
import math

class Curvas(Rasterizacao):
    def __init__(self, ponto_inicial, ponto_final, pontos_controle: list):
        super().__init__(pontos_controle)

        self.pontos = []
        # Calcula a distância entre ponto inicial e final
        distancia = self.calcular_distancia(ponto_inicial, ponto_final)

        # Define o passo com base na distância
        n_pontos = round(distancia)  # Número de pontos proporcional à distância
        passo = 1 / n_pontos
        t = 0.0

        # Gera os pontos usando De Casteljau
        for _ in range(n_pontos + 1):
            self.pontos.append(self.casteljau(t, pontos_controle))
            t += passo

        self.rasterizar_curva()

    def calcular_distancia(self, p1, p2):
        """Calcula a distância euclidiana entre dois pontos."""
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    def casteljau(self, t, pontos_controle):
        """Aplica o algoritmo de De Casteljau para interpolar os pontos de controle."""
        pts = [list(p) for p in pontos_controle]

        # Interpolação entre pontos de controle
        for i in range(1, len(pts)):
            for j in range(len(pts) - i):
                pts[j][0] = (1 - t) * pts[j][0] + t * pts[j + 1][0]
                pts[j][1] = (1 - t) * pts[j][1] + t * pts[j + 1][1]

        # Retorna o ponto interpolado como inteiro
        return [int(pts[0][0]), int(pts[0][1])]

    def rasterizar_curva(self):
        """Conecta os pontos da curva com o algoritmo de Bresenham."""
        for i in range(len(self.pontos) - 1):
            linha = Bresenham(self.pontos[i], self.pontos[i + 1])
            self.saida.extend(linha.saida)  # Adiciona os pontos da linha à saída
