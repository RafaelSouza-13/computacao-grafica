from PIL import Image

class ConversaoMedia:

    def rgb_para_cinza(self, imagem):
        largura, altura = imagem.size
        imagem_cinza = Image.new('L', (largura, altura))

        for x in range(largura):
            for y in range(altura):
                r, g, b = imagem.getpixel((x, y))
                # Calcula a média dos valores RGB
                media = int((r + g + b) / 3)
                # Define o pixel em tons de cinza
                imagem_cinza.putpixel((x, y), media)

        return imagem_cinza

    def cinza_para_binario(self, imagem_cinza):
        largura, altura = imagem_cinza.size
        imagem_binaria = Image.new('L', (largura, altura))
        total = 0

        # Calcular a soma dos pixels
        for x in range(largura):
            for y in range(altura):
                total += imagem_cinza.getpixel((x, y))

        # Calcular o limiar (média)
        limiar = total // (largura * altura)

        # Aplicar o limiar para converter em binário
        for x in range(largura):
            for y in range(altura):
                i = imagem_cinza.getpixel((x, y))  # Usar a imagem_cinza
                # Define o pixel em binário (0 ou 255)
                if i >= limiar:
                    imagem_binaria.putpixel((x, y), 255)  # Branco
                else:
                    imagem_binaria.putpixel((x, y), 0)    # Preto

        return imagem_binaria

    def binario_para_cinza(self, imagem_binaria):
        largura, altura = imagem_binaria.size
        imagem_cinza = Image.new('L', (largura, altura))
        total = 0
        count = 0

        for x in range(largura):
            for y in range(altura):
                valor_binario = imagem_binaria.getpixel((x, y))
                if valor_binario == 255:
                    total += 255
                else:
                    total += 0
                count += 1

        media = total // count

        for x in range(largura):
            for y in range(altura):
                imagem_cinza.putpixel((x, y), media)

        return imagem_cinza

    def cinza_para_rgb(self, imagem_cinza):
        largura, altura = imagem_cinza.size
        imagem_rgb = Image.new('RGB', (largura, altura))

        for x in range(largura):
            for y in range(altura):
                cinza = imagem_cinza.getpixel((x, y))
                imagem_rgb.putpixel((x, y), (cinza, cinza, cinza))

        return imagem_rgb