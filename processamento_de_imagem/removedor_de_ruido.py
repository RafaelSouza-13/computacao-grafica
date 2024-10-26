import cv2
import numpy as np

class RemovedorRuido:
  def remover(self, imagem_path):
    imagem_original = cv2.imread(imagem_path)

    if imagem_original is None:
        print("Erro ao carregar a imagem. Verifique o caminho da imagem.")
        return

    imagem_media = cv2.blur(imagem_original, (5, 5))

    imagem_mediana = cv2.medianBlur(imagem_original, 5)

    imagem_gaussiana = cv2.GaussianBlur(imagem_original, (5, 5), 0)

    cv2.imwrite('imagem_media.jpg', imagem_media)
    cv2.imwrite('imagem_mediana.jpg', imagem_mediana)
    cv2.imwrite('imagem_gaussiana.jpg', imagem_gaussiana)

    cv2.imshow("Imagem Original", imagem_original)
    cv2.imshow("Filtro de Media", imagem_media)
    cv2.imshow("Filtro de Mediana", imagem_mediana)
    cv2.imshow("Filtro Gaussiano", imagem_gaussiana)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
