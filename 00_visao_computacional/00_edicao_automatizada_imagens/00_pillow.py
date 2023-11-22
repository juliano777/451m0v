from PIL.Image import open as PIL_Image_open
from PIL.Image import Transpose as PIL_Image_Transpose
from PIL.ImageOps import invert as PIL_ImageOps_invert

# Cria um objeto de imagem
img = PIL_Image_open('img/phono.jpg')

# Informações da imagem
formato = img.format
modo = img.mode
tamanho = img.size
largura = img.width
altura = img.height

# String com as informações
img_info = f'''\
Formato = {formato}
Modo = {modo}
Tamanho = {tamanho}
Largura = {largura}
Altura = {altura}
'''

# Exibir informações
print(img_info)

# Exibe a imagem
# img.show()

# Tupla com novos valores reduzindo em 50%
novo_tamanho = (
    round(largura / 2),
    round(altura / 2)
    )

# Cria a nova imagem com um novo tamanho
img2 = img.resize(size=novo_tamanho)

# Tupla com os valores para crop
crop_data = (
             5,  # Posição inicial X
             55,  # Posição inicial Y
             264,  # Quantos pixels X para manter
             345  # Quantos pixels Y para manter
             )

# Fazer o corte da imagem com o método crop e os dados da tupla
img2 = img2.crop(crop_data)

# Converter para grayscale
img2 = img2.convert('L')

# Inverter as cores da imagem
img2 = PIL_ImageOps_invert(img2)

# Fazer a transposição rotacionando 180°
img2 = img2.transpose(PIL_Image_Transpose.ROTATE_180)

# Rotacionar 15°
img2 = img2.rotate(15)

# Salvar a imagem
img2.save('img/phono2.jpg')

# Redimensionar mantendo a proporção
# img2 = img.thumbnail((50,50))

# Exibir a imagem final
img2.show()
