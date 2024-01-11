# _*_ encoding: utf8 _*_

# Imports
from cv2 import destroyAllWindows as cv2_destroyAllWindows
from cv2 import imread as cv2_imread
from cv2 import imshow as cv2_imshow
from cv2 import waitKey as cv2_waitKey

# Carrega a imagem
img = cv2_imread('/tmp/tux.png')

# Exibe a imagem
cv2_imshow('Titulo da imagem', img)

# Espera o usuário pressionar uma tecla
cv2_waitKey(0)

# Fecha todas as janelas
cv2_destroyAllWindows()
