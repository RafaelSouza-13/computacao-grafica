from src.primitivas_graficas import Rasterizacao

class Circulo(Rasterizacao):
    def __init__(self, centro, raio):
        super().__init__([centro, raio])
        self.centro = centro
        self.raio = round(raio)
        self.rasterizar_circulo()

    def rasterizar_circulo(self):
        x = 0
        y = self.raio
        erro = -self.raio
        self.adicionar_octantes(x, y)

        while x <= y:
            erro = self.calcular_proximo_erro(x, y, erro)
            x += 1
            if erro >= 0:
                erro = self.ajustar_erro_final(x, y, erro)
                y -= 1
            self.adicionar_octantes(x, y)

    def calcular_proximo_erro(self, x, y, erro):
        return erro + 2 * x + 1

    def ajustar_erro_final(self, x, y, erro):
        return erro - 2 * y + 2

    def adicionar_octantes(self, x, y):
        cx, cy = self.centro
        self.saida.append([cx + x, cy + y])
        self.saida.append([cx + y, cy + x])
        self.saida.append([cx + y, cy - x])
        self.saida.append([cx + x, cy - y])
        self.saida.append([cx - x, cy - y])
        self.saida.append([cx - y, cy - x])
        self.saida.append([cx - y, cy + x])
        self.saida.append([cx - x, cy + y])