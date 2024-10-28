class PontoCritico:
    def __init__(self, index, direcao, x_interseccao, inv_slope):
        self.index = index
        self.direcao = direcao
        self.x_interseccao = x_interseccao
        self.inv_slope = inv_slope

    def __lt__(self, outro):
        return self.x_interseccao < outro.x_interseccao