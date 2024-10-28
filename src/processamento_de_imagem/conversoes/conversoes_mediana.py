from PIL import Image
import numpy as np

class ConversaoMediana:

    def rgb_para_cinza(self, imagem):
        largura, altura = imagem.size
        imagem_cinza = Image.new('L', (largura, altura))

        for x in range(largura):
            for y in range(altura):
                pixels = []
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < largura and 0 <= ny < altura:
                            r, g, b = imagem.getpixel((nx, ny))
                            pixels.append((r + g + b) // 3)

                mediana = sorted(pixels)[len(pixels) // 2]

                imagem_cinza.putpixel((x, y), mediana)

        return imagem_cinza

    def cinza_para_binario(self, imagem_cinza):
        largura, altura = imagem_cinza.size
        pixels = []

        for x in range(largura):
            for y in range(altura):
                pixel = imagem_cinza.getpixel((x, y))
                pixels.append(pixel)

        mediana = np.median(pixels)

        imagem_binaria = Image.new('L', (largura, altura))

        for x in range(largura):
            for y in range(altura):
                pixel = imagem_cinza.getpixel((x, y))
                if pixel >= mediana:
                    imagem_binaria.putpixel((x, y), 255)  # Branco
                else:
                    imagem_binaria.putpixel((x, y), 0)  # Preto

        return imagem_binaria

    def binario_para_cinza(self, imagem_binaria):
        largura, altura = imagem_binaria.size
        imagem_cinza = Image.new('L', (largura, altura))
        pixel_values = []

        for x in range(largura):
            for y in range(altura):
                pixel_values.append(imagem_binaria.getpixel((x, y)))

        mediana = np.median(pixel_values)
        for x in range(largura):
            for y in range(altura):
                pixel = imagem_binaria.getpixel((x, y))
                imagem_cinza.putpixel((x, y), int(mediana))

        return imagem_cinza

    def cinza_para_rgb(self, imagem_cinza):
        largura, altura = imagem_cinza.size
        imagem_rgb = Image.new('RGB', (largura, altura))

        for x in range(largura):
            for y in range(altura):
                cinza = imagem_cinza.getpixel((x, y))
                imagem_rgb.putpixel((x, y), (cinza, cinza, cinza))

        return imagem_rgb