# este script toma fotos de la webcam y las agrega automaticamente a la carpeta de entrenamiento
import cv2
import os
import time

# Directorio de destino para las imágenes
output_directory = 'dataset/walking_people'

# Crear el directorio si no existe
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Configuración de la cámara
camera = cv2.VideoCapture(0)  # Usa el índice 0 para la cámara predeterminada

# Contador de imágenes
image_count = 0

# Intervalo de tiempo entre capturas (en segundos)
capture_interval = 5

# Variables de control para el contador
last_capture_time = time.time()
counter = 0

# Bucle principal
while True:
    # Leer imagen desde la cámara
    ret, frame = camera.read()

    # Mostrar la imagen en una ventana
    cv2.imshow('Webcam', frame)

    # Esperar 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Capturar imagen cada cierto intervalo de tiempo
    current_time = time.time()
    if current_time - last_capture_time >= capture_interval:
        last_capture_time = current_time

        # Guardar imagen en el directorio de destino
        image_path = os.path.join(output_directory, f'image{image_count}.jpg')
        cv2.imwrite(image_path, frame)

        print(f'Imagen guardada: {image_path}')
        image_count += 1
        
        # Imprimir contador
        counter += 1
        print(f'Fotos tomadas: {counter}')

# Liberar recursos
camera.release()
cv2.destroyAllWindows()
