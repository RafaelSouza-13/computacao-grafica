import os

import cv2
from src.processamento_de_imagem import ConversorGerenciador, GeradorImagem
from src.processamento_de_imagem import NoiseRemover
from src.processamento_de_imagem import EdgeHighlighter

gerador = GeradorImagem()
conversor = ConversorGerenciador('media')
nome = 'quadro_pixels'
imagem = gerador.criar_imagem(nome, 25, 25, 'png')
current_directory = os.getcwd()

rgb_para_cinza = conversor.rgb_para_cinza(imagem)

# Conversão com a média
gerador.salvar_imagem(rgb_para_cinza, nome+'_rgb_para_cinza_media', 'png', 'media')

cinza_para_binaria = conversor.cinza_para_binaria(rgb_para_cinza)
gerador.salvar_imagem(cinza_para_binaria, nome+'_cinza_para_binaria_media', 'png', 'media')

binaria_para_cinza = conversor.binario_para_cinza(cinza_para_binaria)
gerador.salvar_imagem(binaria_para_cinza, nome+'_binaria_para_cinza_media', 'png', 'media')

cinza_para_rgb = conversor.cinza_para_rgb(binaria_para_cinza)
gerador.salvar_imagem(cinza_para_rgb, nome+'_cinza_para_rgb_media', 'png', 'media')

# Conversão com a mediana
conversor.tipo_conversao = "mediana"

rgb_para_cinza = conversor.rgb_para_cinza(imagem)
gerador.salvar_imagem(rgb_para_cinza, nome+'_rgb_para_cinza_mediana', 'png', 'mediana')

cinza_para_binaria = conversor.cinza_para_binaria(rgb_para_cinza)
gerador.salvar_imagem(cinza_para_binaria, nome+'_cinza_para_binaria_mediana', 'png', 'mediana')

binaria_para_cinza = conversor.binario_para_cinza(cinza_para_binaria)
gerador.salvar_imagem(binaria_para_cinza, nome+'_binaria_para_cinza_mediana', 'png', 'mediana')

cinza_para_rgb_media = conversor.cinza_para_rgb(binaria_para_cinza)
gerador.salvar_imagem(cinza_para_rgb_media, nome+'_cinza_para_rgb_mediana', 'png', 'mediana')

# Conversão com a Gausianno
imagem_gausianno_path = os.path.join(current_directory, "src", "images", "imagem-gausianno.png")
imagem_gausianno = cv2.imread(imagem_gausianno_path)

conversor.tipo_conversao = "gausianno"

rgb_para_cinza = conversor.rgb_para_cinza(imagem_gausianno)

imagem_gausianno_path = os.path.join(current_directory, "src", "images", "result", "gausianno", "gausianno-rgb-para-cinza.png")
cv2.imwrite(imagem_gausianno_path, rgb_para_cinza)

cinza_para_binaria = conversor.cinza_para_binaria(rgb_para_cinza)

imagem_gausianno_path = os.path.join(current_directory, "src", "images", "result", "gausianno", "gausianno-cinza-para-binario.png")
cv2.imwrite(imagem_gausianno_path, cinza_para_binaria)

noise_image_path = os.path.join(current_directory, "src", "images", "imagem-com-ruido.png")
noise_remover = NoiseRemover()
noise_remover.execute(noise_image_path)

highlighter_image_path = os.path.join(current_directory, "src", "images", "imagem-bordas.png")
edge_highlighter = EdgeHighlighter()
edge_highlighter.execute(highlighter_image_path)