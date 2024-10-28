from PIL import Image
import numpy as np
import math

class ConversaoGaussiana:
    def __init__(self, kernel_size=5, sigma=1):
        self.kernel_size = kernel_size
        self.sigma = sigma
        self.kernel = self.gaussian_kernel(kernel_size, sigma)

    def rgb_para_cinza(self, imagem, conversor):
        imagem_cinza = conversor.rgb_para_cinza(imagem)
        imagem_suavizada = self.apply_gaussian_blur(imagem_cinza)
        return imagem_suavizada



    def gaussian_kernel(self, size, sigma=0):
        kernel = np.zeros((size, size), dtype=np.float64)
        mean = size // 2
        sum_val = 0.0

        for x in range(size):
            for y in range(size):
                kernel[x, y] = (1 / (2 * math.pi * sigma ** 2)) * math.exp(
                    -((x - mean) ** 2 + (y - mean) ** 2) / (2 * sigma ** 2))
                sum_val += kernel[x, y]

        kernel /= sum_val
        return kernel

    def apply_kernel(self, imagem):
        result = 0.0
        for i in range(self.kernel_size):
            for j in range(self.kernel_size):
                result += imagem[i, j] * self.kernel[i, j]
        return result

    def apply_gaussian_blur(self, imagem):
        height, width = imagem.shape
        blurred_image = np.zeros_like(imagem)

        for i in range(self.kernel_size // 2, height - self.kernel_size // 2):
            for j in range(self.kernel_size // 2, width - self.kernel_size // 2):
                pixel_grid = imagem[i - self.kernel_size // 2:i + self.kernel_size // 2 + 1,
                                   j - self.kernel_size // 2:j + self.kernel_size // 2 + 1]
                blurred_image[i, j] = self.apply_kernel(pixel_grid)
        return blurred_image

    def cinza_para_binario(self, imagem_cinza):
        pass