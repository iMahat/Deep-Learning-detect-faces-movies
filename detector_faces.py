# Import de bibliotecas
import cv2 #Processador de imagens/vídeos
import face_recognition #Biblioteca de Reconhecimento Facial

# Obtendo referência da webcam 
captura_video = cv2.VideoCapture(0) # Zero especifica que será usada a webcam integrada

# Inicializando variáveis
face_locations = []

while True:
    # Captura de um único quadro (frame) por vez
    ret, frame = captura_video.read()

    # Conversor de cor BGR [usado pelo 'OpenCV (cv2)'] para RGB (usado pelo 'face_recognition')
    rgb_frame = frame[:, :, ::-1]

    # Encontrando rostos no quadro atual
    face_locations = face_recognition.face_locations(rgb_frame)

    # Mostrar resultados
    for top, right, bottom, left in face_locations:
        # Desenhando um quadrado ao redor do rosto
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    # Mostrar a imagem resultante
    cv2.imshow('Video', frame)

    # Configurando a tecla "s" para sair do programa
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

# Liberar webcam ou fonte de vídeo
captura_video.release()
cv2.destroyAllWindows()