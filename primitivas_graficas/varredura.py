from primitivas_graficas import Rasterizacao, PontoCritico

class Varredura(Rasterizacao):
    def __init__(self, poligono):
        super().__init__(poligono)
        self.ymin, self.ymax = self.definir_limites(poligono)
        self.pontos_criticos = self.encontrar_pontos_criticos(poligono)
        self.preencher_poligono(poligono)

    def definir_limites(self, poligono):
        ymin = min(p[1] for p in poligono)
        ymax = max(p[1] for p in poligono)
        return ymin, ymax

    def encontrar_pontos_criticos(self, poligono):
        pts_criticos = []

        for i in range(len(poligono)):
            prox_ponto = poligono[(i + 1) % len(poligono)]
            prev_ponto = poligono[(i - 1) % len(poligono)]

            if poligono[i][1] < prox_ponto[1]:
                inv_slope = (prox_ponto[0] - poligono[i][0]) / (prox_ponto[1] - poligono[i][1])
                pts_criticos.append(PontoCritico(i, direcao=1, x_interseccao=poligono[i][0], inv_slope=inv_slope))

            if poligono[i][1] < prev_ponto[1]:
                inv_slope = (prev_ponto[0] - poligono[i][0]) / (prev_ponto[1] - poligono[i][1])
                pts_criticos.append(PontoCritico(i, direcao=-1, x_interseccao=poligono[i][0], inv_slope=inv_slope))

        return pts_criticos

    def preencher_poligono(self, poligono):
        ativos = []

        for y in range(self.ymin, self.ymax + 1):
            for ponto in ativos:
                ponto.x_interseccao += ponto.inv_slope

            ativos.extend(pt for pt in self.pontos_criticos if poligono[pt.index][1] == y)
            ativos = [p for p in ativos if poligono[(p.index + p.direcao + len(poligono)) % len(poligono)][1] != y]

            ativos.sort()

            for i in range(0, len(ativos), 2):
                xmin = round(ativos[i].x_interseccao)
                xmax = round(ativos[i + 1].x_interseccao)
                self.saida.extend([[x, y] for x in range(xmin, xmax)])