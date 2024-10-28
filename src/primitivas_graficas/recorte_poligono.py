from src.primitivas_graficas import Rasterizacao, Polilinha


class RecortePoligono(Rasterizacao):
    def __init__(self, pts_poligono: list, x_min, x_max, y_min, y_max):
        super().__init__([pts_poligono, x_min, x_max, y_min, y_max])
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

        esquerda = self.sutherland_hodgman_esq(pts_poligono)
        cima = self.sutherland_hodgman_cima(esquerda)
        direita = self.sutherland_hodgman_dir(cima)
        baixo = self.sutherland_hodgman_baixo(direita)

        novo_poligono_vertices = baixo
        poligono = Polilinha(novo_poligono_vertices, fechar=True)
        self.saida = poligono.saida

    def sutherland_hodgman_esq(self, pts):
        novo_poligono = []
        for i in range(len(pts)):
            p1 = pts[i]
            p2 = pts[(i + 1) % len(pts)]

            x1, y1 = p1
            x2, y2 = p2

            if x1 >= self.x_min:
                if x2 >= self.x_min:
                    novo_poligono.append(list(p2))
                else:
                    novo_poligono.append([
                        self.x_min,
                        round(y1 + (y2 - y1) * (self.x_min - x1) / (x2 - x1))
                    ])
            else:
                if x2 >= self.x_min:
                    novo_poligono.append([
                        self.x_min,
                        round(y1 + (y2 - y1) * (self.x_min - x1) / (x2 - x1))
                    ])
                    novo_poligono.append(p2)
        return novo_poligono

    def sutherland_hodgman_dir(self, pts):
        novo_poligono = []
        for i in range(len(pts)):
            p1 = pts[i]
            p2 = pts[(i + 1) % len(pts)]

            x1, y1 = p1
            x2, y2 = p2

            if x1 <= self.x_max:
                if x2 <= self.x_max:
                    novo_poligono.append(list(p2))
                else:
                    novo_poligono.append([
                        self.x_max,
                        round(y1 + (y2 - y1) * (self.x_max - x1) / (x2 - x1))
                    ])
            else:
                if x2 <= self.x_max:
                    novo_poligono.append([
                        self.x_max,
                        round(y1 + (y2 - y1) * (self.x_max - x1) / (x2 - x1))
                    ])
                    novo_poligono.append(p2)
        return novo_poligono

    def sutherland_hodgman_baixo(self, pts):
        novo_poligono = []
        for i in range(len(pts)):
            p1 = pts[i]
            p2 = pts[(i + 1) % len(pts)]

            x1, y1 = p1
            x2, y2 = p2

            if y1 >= self.y_min:
                if y2 >= self.y_min:
                    novo_poligono.append(list(p2))
                else:
                    novo_poligono.append([
                        round(x1 + (x2 - x1) * (self.y_min - y1) / (y2 - y1)),
                        self.y_min
                    ])
            else:
                if y2 >= self.y_min:
                    novo_poligono.append([
                        round(x1 + (x2 - x1) * (self.y_min - y1) / (y2 - y1)),
                        self.y_min
                    ])
                    novo_poligono.append(p2)
        return novo_poligono

    def sutherland_hodgman_cima(self, pts):
        novo_poligono = []
        for i in range(len(pts)):
            p1 = pts[i]
            p2 = pts[(i + 1) % len(pts)]

            x1, y1 = p1
            x2, y2 = p2

            if y1 <= self.y_max:
                if y2 <= self.y_max:
                    novo_poligono.append(list(p2))
                else:
                    novo_poligono.append([
                        round(x1 + (x2 - x1) * (self.y_max - y1) / (y2 - y1)),
                        self.y_max
                    ])
            else:
                if y2 <= self.y_max:
                    novo_poligono.append([
                        round(x1 + (x2 - x1) * (self.y_max - y1) / (y2 - y1)),
                        self.y_max
                    ])
                    novo_poligono.append(p2)
        return novo_poligono
