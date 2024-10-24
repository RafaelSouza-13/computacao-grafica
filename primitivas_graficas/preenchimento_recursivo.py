from primitivas_graficas import Rasterizacao
from interface.grid import Grid

class PreenchimentoRecursivo(Rasterizacao):
  def __init__(self, ponto, cor, cor_borda, tela: Grid):
    super().__init__([ponto, cor, tela])
    self.tela = tela
    self.cor = cor
    self.cor_borda = cor_borda
    self.recursao(ponto)

  def recursao(self, ponto):
    ponto_atual = ponto
    cor_atual = self.tela.checar_matriz(ponto_atual[0], ponto_atual[1])

    if cor_atual != self.cor and cor_atual != self.cor_borda:
      self.tela.desenhar_pixel(ponto_atual[0], ponto_atual[1], self.cor)
      self.recursao((ponto_atual[0] + 1, ponto_atual[1]))
      self.recursao((ponto_atual[0], ponto_atual[1] + 1))
      self.recursao((ponto_atual[0] - 1, ponto_atual[1]))
      self.recursao((ponto_atual[0], ponto_atual[1] - 1))