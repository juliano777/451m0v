from PIL.Image import open as PIL_Image_open
from PIL.Image import Transpose as PIL_Image_Transpose
# Cria um objeto de imagem
img = PIL_Image_open('img/image.jpg')

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

# Redimensionar a imagem em 50%
novo_tamanho = (
    round(largura / 10),
    round(altura / 10)
    )

img2 = img.resize(size=novo_tamanho)

crop_data = (0, 0, 10, 200)
img.crop()

img2.save('/tmp/teste.jpg')
#img.show()

img.rotate(15)

img.transpose(PIL_Image_Transpose.ROTATE_180)


img.thumbnail((50,50))
img