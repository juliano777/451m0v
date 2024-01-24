# _*_ encoding: utf-8 _*_

from cv2 import COLOR_BGR2GRAY as cv2_COLOR_BGR2GRAY
from cv2 import imread as cv2_imread
from cv2 import imshow as cv2_imshow
from cv2 import cvtColor as cv2_cvtColor
from cv2 import waitKey as cv2_waitKey

# Lendo imagens - 3 canais
cat = cv2_imread('../assets/fotos/cat.jpg')
park = cv2_imread('../assets/fotos/park.jpg')

# Converter para escala de cinza
grey_cat = cv2_cvtColor(cat, cv2_COLOR_BGR2GRAY)

# Exibir a imagem em escala de cinza
cv2_imshow('Gato em cores', cat)

# Exibir a imagem em escala de cinza
cv2_imshow('Gato em escala de cinza', grey_cat)

# Espera o usuário pressionar uma tecla
cv2_waitKey(0)
