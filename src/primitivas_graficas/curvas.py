from src.primitivas_graficas import Rasterizacao, Bresenham
import math

class Curvas(Rasterizacao):
    def __init__(self, ponto_inicial, ponto_final, pontos_controle: list):
        super().__init__(pontos_controle)

        self.pontos = []
        distancia = self.calcular_distancia(ponto_inicial, ponto_final)

        n_pontos = round(distancia)
        passo = 1 / n_pontos
        t = 0.0

        for _ in range(n_pontos + 1):
            self.pontos.append(self.casteljau(t, pontos_controle))
            t += passo

        self.rasterizar_curva()

    def calcular_distancia(self, p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    def casteljau(self, t, pontos_controle):
        pts = [list(p) for p in pontos_controle]

        for i in range(1, len(pts)):
            for j in range(len(pts) - i):
                pts[j][0] = (1 - t) * pts[j][0] + t * pts[j + 1][0]
                pts[j][1] = (1 - t) * pts[j][1] + t * pts[j + 1][1]

        return [int(pts[0][0]), int(pts[0][1])]

    def rasterizar_curva(self):
        for i in range(len(self.pontos) - 1):
            linha = Bresenham(self.pontos[i], self.pontos[i + 1])
            self.saida.extend(linha.saida)
