# _*_ encoding: utf-8 _*_

# Imports
from cv2 import VideoCapture as cv2_VideoCapture
from cv2 import destroyAllWindows as cv2_destroyAllWindows
from cv2 import imshow as cv2_imshow
from cv2 import waitKey as cv2_waitKey

# Objeto de captura de vídeo
cam = cv2_VideoCapture(0)

while True:

    # Captura de vídeo quadro a quadro
    _, frame = cam.read()

    # Exibe o quadro resultante
    cv2_imshow('frame', frame)

    # Definindo a tecla 'q' para parar o vídeo
    if cv2_waitKey(1) & 0xFF == ord('q'):
        break

# Após o fim do loop liberar o objeto de captura
cam.release()

# Fecha todas janelas
cv2_destroyAllWindows()
