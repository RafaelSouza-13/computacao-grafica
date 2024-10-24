from primitivas_graficas import Rasterizacao

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
        self.adicionar_octantes(x, y)  # Inicialmente adiciona os octantes com (0, raio)

        # Algoritmo de ponto médio para desenhar o círculo
        while x <= y:
            erro = self.calcular_proximo_erro(x, y, erro)
            x += 1
            if erro >= 0:
                erro = self.ajustar_erro_final(x, y, erro)
                y -= 1
            self.adicionar_octantes(x, y)

    def calcular_proximo_erro(self, x, y, erro):
        """Calcula o próximo valor do erro."""
        return erro + 2 * x + 1

    def ajustar_erro_final(self, x, y, erro):
        """Ajusta o erro ao trocar a coordenada y."""
        return erro - 2 * y + 2

    def adicionar_octantes(self, x, y):
        """Adiciona os pontos correspondentes aos 8 octantes do círculo."""
        cx, cy = self.centro
        # Adiciona os 8 pontos simétricos ao longo dos octantes
        self.saida.append([cx + x, cy + y])
        self.saida.append([cx + y, cy + x])
        self.saida.append([cx + y, cy - x])
        self.saida.append([cx + x, cy - y])
        self.saida.append([cx - x, cy - y])
        self.saida.append([cx - y, cy - x])
        self.saida.append([cx - y, cy + x])
        self.saida.append([cx - x, cy + y])