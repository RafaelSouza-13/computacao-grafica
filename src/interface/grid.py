from tkinter import *

class Grid:
  def __init__(self, tamanho_tela):
    self.tamanho_tela = tamanho_tela
    self.matriz = []
    self.tamanho_matriz = 50
    self.tamanho_pixel = int(self.tamanho_tela / self.tamanho_matriz)

    for i in range(self.tamanho_matriz):
        linha = []
        for j in range(self.tamanho_matriz):
          linha.append(0)
        self.matriz.append(linha)

    self.master = Tk()
    self.tela = Canvas(self.master,
                       width=self.tamanho_tela,
                       height=self.tamanho_tela)
    self.tela.pack()
    self.CriarTemplate()

  def CriarTemplate(self):
    aux = int(self.tamanho_tela / 2) + (self.tamanho_pixel / 2)

    for x in range(0, self.tamanho_tela, self.tamanho_pixel):
      self.tela.create_line(x, 0, x, self.tamanho_tela, fill='#DCDCDC')

    for y in range(0, self.tamanho_tela, self.tamanho_pixel):
      self.tela.create_line(0, y, self.tamanho_tela, y, fill='#DCDCDC')

    self.tela.create_line(0,
                          aux - self.tamanho_pixel,
                          self.tamanho_tela,
                          aux - self.tamanho_pixel,
                          fill="#f00")
    self.tela.create_line(aux, 0, aux, self.tamanho_tela,
                          fill="#f00")

  def converter_coordenadas(self, x, y):
    real_x = int((self.tamanho_pixel * x) + (self.tamanho_tela / 2))
    real_y = int((self.tamanho_tela / 2) - (self.tamanho_pixel * y))

    return real_x, real_y

  def converter_coordenadas_matriz(self, x, y):
    coluna = int(x + (self.tamanho_matriz / 2))
    linha = int((self.tamanho_matriz / 2) - y) - 1

    return linha, coluna

  def desenhar_pixel(self, x, y, cor):
    x1, y1 = self.converter_coordenadas(x, y)
    self.tela.create_rectangle(x1,
                               y1,
                               x1 + self.tamanho_pixel,
                               y1 - self.tamanho_pixel,
                               fill=cor)

    l, c = self.converter_coordenadas_matriz(x, y)
    self.matriz[l][c] = cor

  def desenhar(self, objeto: list, cor):
    for p in objeto:
      self.desenhar_pixel(p[0], p[1], cor)

  def print_matriz(self):
    for linha in self.matriz:
      print(linha)

  def checar_matriz(self, x, y):
    l, c = self.converter_coordenadas_matriz(x, y)
    return self.matriz[l][c]

  def destacar_janela(self, xmin, xmax, ymin, ymax):
    xmin, ymin = self.converter_coordenadas(xmin, ymin)
    xmax, ymax = self.converter_coordenadas(xmax + 1, ymax + 1)
    self.tela.create_rectangle(xmin, ymin, xmax, ymax, outline='green')