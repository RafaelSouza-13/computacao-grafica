from primitivas_graficas import Rasterizacao

class Bresenham(Rasterizacao):
    def __init__(self, ponto1, ponto2):
        super().__init__([ponto1, ponto2])
        self.x_inicial, self.y_inicial = ponto1
        self.x_final, self.y_final = ponto2


        self.pontosFinais = []
        self.trocaX = self.trocaY = self.trocaXY = False

        if ponto1 == ponto2:  # Caso trivial
            self.saida = [ponto1]
            return

        self.calcular_octante()

        deltaX = self.x_final - self.x_inicial
        deltaY = self.y_final - self.y_inicial

        m = deltaY / deltaX if deltaX != 0 else float('inf')
        erro = m - 0.5

        auxX, auxY = self.x_inicial, self.y_inicial
        self.pontosFinais.append([auxX, auxY])

        while auxX < self.x_final:
            if erro >= 0:
                auxY += 1
                erro -= 1
            auxX += 1
            erro += m
            self.pontosFinais.append([auxX, auxY])

        self.aplicar_reflexao(self.pontosFinais)
        self.saida = self.pontosFinais

    def calcular_octante(self):
        deltaX = self.x_final - self.x_inicial
        deltaY = self.y_final - self.y_inicial

        m = deltaY / deltaX if deltaX != 0 else 2

        if abs(m) > 1:
            self.x_inicial, self.y_inicial = self.y_inicial, self.x_inicial
            self.x_final, self.y_final = self.y_final, self.x_final
            self.trocaXY = True

        if self.x_inicial > self.x_final:
            self.x_inicial, self.x_final = -self.x_inicial, -self.x_final
            self.trocaX = True

        if self.y_inicial > self.y_final:
            self.y_inicial, self.y_final = -self.y_inicial, -self.y_final
            self.trocaY = True

    def aplicar_reflexao(self, pontos: list):
        for ponto in pontos:
            if self.trocaY:
                ponto[1] = -ponto[1]
            if self.trocaX:
                ponto[0] = -ponto[0]
            if self.trocaXY:
                ponto[0], ponto[1] = ponto[1], ponto[0]