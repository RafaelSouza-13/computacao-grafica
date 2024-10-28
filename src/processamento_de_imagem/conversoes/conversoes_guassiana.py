from PIL import Image
import numpy as np
import math
import cv2

class ConversaoGaussiana:
    def rgb_para_cinza(self, imagem):
        if imagem is None:
            print("Image not found.")
            return

        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        imagem_cinza_gaussiana = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)

        return imagem_cinza_gaussiana

    def cinza_para_binario(self, imagem):
        if imagem is None:
            print("Image not found.")
            return

        imagem_binaria = cv2.adaptiveThreshold(imagem, 255,
                                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY,
                                            11, 2)

        return imagem_binaria
