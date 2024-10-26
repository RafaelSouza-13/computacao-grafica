import os
import cv2
import numpy as np

class RemovedorRuido:
  def remover(self, imagem_path):
    path_parcial = imagem_path.replace("imagem-com-ruido.png", "")
    path_resultado = os.path.join(path_parcial, "resultado", "removedor-ruido")

    imagem_original = cv2.imread(imagem_path)

    if imagem_original is None:
        print("Erro ao carregar a imagem. Verifique o caminho da imagem.")
        return

    imagem_media = cv2.blur(imagem_original, (5, 5))
    imagem_mediana = cv2.medianBlur(imagem_original, 5)
    imagem_gaussiana = cv2.GaussianBlur(imagem_original, (5, 5), 0)

    path_resultado_media = os.path.join(path_resultado, "ruido_resultado_media.jpg")
    cv2.imwrite(path_resultado_media, imagem_media)

    path_resultado_mediana = os.path.join(path_resultado, "ruido_resultado_mediana.jpg")
    cv2.imwrite(path_resultado_mediana, imagem_mediana)

    path_resultado_gaussiana = os.path.join(path_resultado, "ruido_resultado_gaussiana.jpg")
    cv2.imwrite(path_resultado_gaussiana, imagem_gaussiana)

    cv2.imshow("Imagem Original", imagem_original)
    cv2.imshow("Filtro de Media", imagem_media)
    cv2.imshow("Filtro de Mediana", imagem_mediana)
    cv2.imshow("Filtro Gaussiano", imagem_gaussiana)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
