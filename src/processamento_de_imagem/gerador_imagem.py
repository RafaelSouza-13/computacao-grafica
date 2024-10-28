from PIL import Image, ImageFilter
import random
import os

class GeradorImagem:
    def criar_imagem(self, nome, largura, altura, formato):
        # Cria uma nova imagem RGB
        imagem = Image.new('RGB', (largura, altura))
        for x in range(largura):
            for y in range(altura):
                # Gera uma cor RGB aleatória
                cor_aleatoria = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                imagem.putpixel((x, y), cor_aleatoria)

        return self.salvar_imagem(imagem, nome, formato)


    def salvar_imagem(self, imagem, nome, formato, path=""):
        os.makedirs(f'images_geradas/{path}', exist_ok=True)
        path = os.path.join(f'images_geradas/{path}', f"{nome}.{formato.lower()}")
        imagem.save(path)
        return imagem

    def exibir_imagem(self, imagem):
        imagem.show()