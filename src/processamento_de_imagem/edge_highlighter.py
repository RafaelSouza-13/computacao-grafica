import os
import cv2
import numpy as np

class EdgeHighlighter:
  def execute(self, imagem_path):
    partial_path = imagem_path.replace("imagem-bordas.png", "")
    path_resultado = os.path.join(partial_path, "result", "edge-highlighter")

    image = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("It was not possible to load image.")
        return

    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    bordas_sobel = cv2.magnitude(sobelx, sobely)

    kernel_prewitt_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=np.float32)
    kernel_prewitt_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)
    prewittx = cv2.filter2D(image, -1, kernel_prewitt_x)  # Aplicando kernel x
    prewitty = cv2.filter2D(image, -1, kernel_prewitt_y)  # Aplicando kernel y
    bordas_prewitt = cv2.magnitude(prewittx.astype(np.float32), prewitty.astype(np.float32))

    bordas_canny = cv2.Canny(image, 100, 200)

    path_result_sobel = os.path.join(path_resultado, "highlight_result_sobel.jpg")
    cv2.imwrite(path_result_sobel, bordas_sobel)

    path_result_prewitt = os.path.join(path_resultado, "highlight_result_prewitt.jpg")
    cv2.imwrite(path_result_prewitt, bordas_prewitt)

    path_result_canny = os.path.join(path_resultado, "highlight_result_canny.jpg")
    cv2.imwrite(path_result_canny, bordas_canny)

    # Exibir os resultados
    cv2.imshow("Imagem Original", image)
    cv2.imshow("Bordas Sobel", bordas_sobel / bordas_sobel.max())  # Normalizar para exibição
    cv2.imshow("Bordas Prewitt", bordas_prewitt / bordas_prewitt.max())  # Normalizar para exibição
    cv2.imshow("Bordas Canny", bordas_canny)

    # Espera até que uma tecla seja pressionada e fecha as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()