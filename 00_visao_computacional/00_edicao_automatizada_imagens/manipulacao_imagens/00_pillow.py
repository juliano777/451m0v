from PIL.Image import open as PIL_Image_open

# Cria um objeto de imagem
img = PIL_Image_open('img/image.jpg')

# Exibe a imagem
img.show()

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

img


# Exibir informações
print(img_info)
