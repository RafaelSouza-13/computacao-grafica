from src.primitivas_graficas import Rasterizacao, Polilinha

class RecortePoligono(Rasterizacao):
    def __init__(self, pts_poligono: list, x_min, x_max, y_min, y_max):
        super().__init__([pts_poligono, x_min, x_max, y_min, y_max])
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

        recorte = self.sutherland_hodgman(pts_poligono)
        self.saida = Polilinha(recorte, fechar=True).saida

    def sutherland_hodgman(self, pts):
        for lado in [self.sutherland_hodgman_esq, self.sutherland_hodgman_dir,
                     self.sutherland_hodgman_baixo, self.sutherland_hodgman_cima]:
            pts = lado(pts)
        return pts

    def sutherland_hodgman_esq(self, pts):
        return self.sutherland_hodgman_lado(pts, self.x_min, lambda x1, y1, x2, y2: 
            (self.x_min, y1 + (y2 - y1) * (self.x_min - x1) / (x2 - x1)))

    def sutherland_hodgman_dir(self, pts):
        return self.sutherland_hodgman_lado(pts, self.x_max, lambda x1, y1, x2, y2: 
            (self.x_max, y1 + (y2 - y1) * (self.x_max - x1) / (x2 - x1)))

    def sutherland_hodgman_baixo(self, pts):
        return self.sutherland_hodgman_lado(pts, self.y_min, lambda x1, y1, x2, y2: 
            (x1 + (x2 - x1) * (self.y_min - y1) / (y2 - y1), self.y_min))

    def sutherland_hodgman_cima(self, pts):
        return self.sutherland_hodgman_lado(pts, self.y_max, lambda x1, y1, x2, y2: 
            (x1 + (x2 - x1) * (self.y_max - y1) / (y2 - y1), self.y_max))

    def sutherland_hodgman_lado(self, pts, limite, calcular_intersecao):
        novo_poligono = []
        for i in range(len(pts)):
            p1, p2 = pts[i], pts[(i + 1) % len(pts)]
            x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]

            if self.is_inside(x1, limite):
                if self.is_inside(x2, limite):
                    novo_poligono.append(p2)
                else:
                    novo_poligono.append(calcular_intersecao(x1, y1, x2, y2))
            elif self.is_inside(x2, limite):
                novo_poligono.append(calcular_intersecao(x1, y1, x2, y2))
                novo_poligono.append(p2)

        return novo_poligono

    def is_inside(self, valor, limite):
        return valor >= limite if limite == self.x_min or limite == self.y_min else valor <= limite