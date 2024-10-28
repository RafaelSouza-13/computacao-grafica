import os
import cv2

class NoiseRemover:
  def execute(self, imagem_path):
    partial_path = imagem_path.replace("imagem-com-ruido.png", "")
    path_result = os.path.join(partial_path, "result", "noise-remover")

    original_image = cv2.imread(imagem_path)

    if original_image is None:
        print("Erro ao carregar a imagem. Verifique o caminho da imagem.")
        return

    mean_image = cv2.blur(original_image, (5, 5))
    median_image = cv2.medianBlur(original_image, 5)
    gaussian_image = cv2.GaussianBlur(original_image, (5, 5), 0)

    path_resultado_media = os.path.join(path_result, "ruido_resultado_media.jpg")
    cv2.imwrite(path_resultado_media, mean_image)

    path_resultado_mediana = os.path.join(path_result, "ruido_resultado_mediana.jpg")
    cv2.imwrite(path_resultado_mediana, median_image)

    path_resultado_gaussiana = os.path.join(path_result, "ruido_resultado_gaussiana.jpg")
    cv2.imwrite(path_resultado_gaussiana, gaussian_image)

    cv2.imshow("Imagem Original", original_image)
    cv2.imshow("Filtro de Media", mean_image)
    cv2.imshow("Filtro de Mediana", median_image)
    cv2.imshow("Filtro Gaussiano", gaussian_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
