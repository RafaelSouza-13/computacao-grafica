from src.processamento_de_imagem.conversoes import *

class ConversorGerenciador:
    def __init__(self, tipo_conversao):
        self.tipo_conversao = tipo_conversao.lower()

    def rgb_para_cinza(self, imagem):
        if self.tipo_conversao == 'media':
            conversor = ConversaoMedia()
            imagem_cinza = conversor.rgb_para_cinza(imagem)
        elif self.tipo_conversao == 'mediana':
            conversor = ConversaoMediana()
            imagem_cinza = conversor.rgb_para_cinza(imagem)
        else:
            raise ValueError("Tipo de conversão inválido.")

        return imagem_cinza

    def cinza_para_binaria(self, imagem_cinza):
        if self.tipo_conversao == 'media':
            conversor = ConversaoMedia()
            imagem_binario = conversor.cinza_para_binario(imagem_cinza)
        elif self.tipo_conversao == 'mediana':
            conversor = ConversaoMediana()
            imagem_binario = conversor.cinza_para_binario(imagem_cinza)
        else:
            raise ValueError("Tipo de conversão inválido.")
        return imagem_binario

    def binario_para_cinza(self, imagem_binaria):
        if self.tipo_conversao == 'media':
            conversor = ConversaoMedia()
            imagem_cinza = conversor.binario_para_cinza(imagem_binaria)
        elif self.tipo_conversao == 'mediana':
            conversor = ConversaoMediana()
            imagem_cinza = conversor.binario_para_cinza(imagem_binaria)
        else:
            raise ValueError("Tipo de conversão inválido.")
        return imagem_cinza

    def cinza_para_rgb(self, imagem_cinza):
        if self.tipo_conversao == 'media':
            conversor = ConversaoMedia()
            imagem_rgb = conversor.cinza_para_rgb(imagem_cinza)
        elif self.tipo_conversao == 'mediana':
            conversor = ConversaoMediana()
            imagem_rgb = conversor.cinza_para_rgb(imagem_cinza)
        else:
            raise ValueError("Tipo de conversão inválido.")
        return imagem_rgb