from tkinter import *
from src.interface.grid import Grid
from src.primitivas_graficas import *

tela = Grid(550)
roxo = '#990099'
rosa = '#FF99DD'

#EXEMPLOS:

#BRESENHAM

linha = Bresenham((2, 3), (4, 9))
tela.desenhar(linha.saida, roxo)

#POLILINHA

# pts = [(0, 8), (8, 0), (0, -8), (-8, 0)]
# linhas = Polilinha(pts, fechar=True)
# tela.desenhar(linhas.saida, roxo)

# TRANSFORMAÇÃO

# pts = [(0, 0), (0, 5), (9, 5), (5, 2), (2, 0)]
# polinomio = Polilinha(pts, fechar=True)
#
# new_polinomio = Transformacao(entrada=polinomio.saida)
# new_polinomio .translacao(5,5)
# #new_polinomio .escalonamento(2, 3)
# #new_polinomio .rotacao([0, 0], 90)
# tela.desenhar(new_polinomio .saida, roxo)

# CIRCULO

# circulo = Circulo((7, 7), 10)
# tela.desenhar(circulo.saida, roxo)

#CURVAS

# grau_1 = Curvas([5, 10], [15, 10], [(5, 10), (10, 20), (15, 10)])
# tela.desenhar(grau_1.saida, roxo)
# grau_2 = Curvas([5, 10], [15, 10], [(5, 10), (8, 3), (12, 18), (15, 10)])
# tela.desenhar(grau_2.saida, roxo)


# PREENCHIMENTO RECURSIVO

# pts = [(0, 8), (8, 0), (0, -8), (-8, 0)]
# obj = Polilinha(pts, fechar=True)
# tela.desenhar(obj.saida, roxo)
# pr = PreenchimentoRecursivo((2,0), rosa, roxo, tela)

#Varredura

# pts = [(0, -12), (-12, 2), (12, 2)]
# obj = Varredura(pts)
# tela.desenhar(obj.saida, roxo)

#RECORTE DE LINHA

# p1, p2 = (-5, 15),(18, 5)
# x_min = 2
# x_max = 20
# y_min = 2
# y_max = 20
# obj = RecorteLinha(p1, p2, x_min, x_max, y_min, y_max)
# tela.destacar_janela(x_min, x_max, y_min, y_max)
# tela.desenhar(obj.saida, roxo)

# #RECORTE DE POLIGONO
#
# #pts = [(0, 8), (8, 0), (0, -8), (-8, 0)]
# pts = [(2, 5), (2, 15), (12, 5)]
#
# x_min = 2
# x_max = 10
# y_min = 5
# y_max = 15
#
# obj = RecortePoligono(pts, x_min, x_max, y_min, y_max)
# tela.destacar_janela(x_min, x_max, y_min, y_max)
# tela.desenhar(obj.saida, roxo)
#
# # poligonoOriginal =  Polilinha(pts, fechar=True)
# # tela.desenhar(poligonoOriginal.saida, rosa)



mainloop()