from src.primitivas_graficas import Rasterizacao, Bresenham

class RecorteLinha(Rasterizacao):
    def __init__(self, ponto_1, ponto_2, x_min, x_max, y_min, y_max):
        super().__init__([ponto_1, ponto_2])
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

        self.ACIMA = int('1000', 2)
        self.ABAIXO = int('0100', 2)
        self.DIREITA = int('0010', 2)
        self.ESQUERDA = int('0001', 2)

        self.cohen_sutherland(list(ponto_1), list(ponto_2))

    def cohen_sutherland(self, ponto_1, ponto_2):
        codigo_p1 = self.calcular_codigo(ponto_1)
        codigo_p2 = self.calcular_codigo(ponto_2)

        while True:
            if codigo_p1 | codigo_p2 == 0:
                linha = Bresenham(ponto_1, ponto_2)
                self.saida = linha.saida
                break
            elif codigo_p1 & codigo_p2 != 0:
                break
            else:
                if codigo_p1 != 0:
                    codigo_fora = codigo_p1
                else:
                    codigo_fora = codigo_p2

                x, y = self.calcular_interseccao(codigo_fora, ponto_1, ponto_2)

                if codigo_fora == codigo_p1:
                    ponto_1[0], ponto_1[1] = x, y
                    codigo_p1 = self.calcular_codigo(ponto_1)
                else:
                    ponto_2[0], ponto_2[1] = x, y
                    codigo_p2 = self.calcular_codigo(ponto_2)

    def calcular_codigo(self, ponto):
        x, y = ponto[0], ponto[1]
        codigo = 0
        if y > self.y_max:
            codigo |= self.ACIMA
        if y < self.y_min:
            codigo |= self.ABAIXO
        if x > self.x_max:
            codigo |= self.DIREITA
        if x < self.x_min:
            codigo |= self.ESQUERDA
        return codigo

    def calcular_interseccao(self, codigo_fora, ponto_1, ponto_2):
        x = None
        y = None
        x1, y1 = ponto_1
        x2, y2 = ponto_2

        if codigo_fora & self.ACIMA:
            x = x1 + (x2 - x1) * (self.y_max - y1) / (y2 - y1)
            y = self.y_max
        elif codigo_fora & self.ABAIXO:
            x = x1 + (x2 - x1) * (self.y_min - y1) / (y2 - y1)
            y = self.y_min
        elif codigo_fora & self.DIREITA:
            y = y1 + (y2 - y1) * (self.x_max - x1) / (x2 - x1)
            x = self.x_max
        elif codigo_fora & self.ESQUERDA:
            y = y1 + (y2 - y1) * (self.x_min - x1) / (x2 - x1)
            x = self.x_min
        return round(x), round(y)