# _*_ encoding: utf8 _*_

from cv2 import VideoCapture as cv2_VideoCapture
from cv2 import destroyAllWindows as cv2_destroyAllWindows
from cv2 import imshow as cv2_imshow
from cv2 import waitKey as cv2_waitKey

# Carrega o video
cap = cv2_VideoCapture('../assets/videos/kitten.mp4')

# Loop enquanto o vídeo é executado
while cap.isOpened():

    # Captura de vídeo quadro a quadro
    _, frame = cap.read()

    # Exibe o quadro atual
    cv2_imshow('Titulo da janela', frame)

    # Definindo a tecla 'q' para parar o vídeo
    if cv2_waitKey(30) & 0xFF == ord('q'):
        break

# Após o fim do loop liberar o objeto de captura
cap.release()

# Fecha todas janelas
cv2_destroyAllWindows()
