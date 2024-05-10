"""
created on 12 Abril 13:28:05 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código carga una imagen, la convierte al espacio HSV, define un rango para identificar el fondo 
y lo elimina creando y aplicando una máscara. Esto es útil para tareas como eliminación de fondo, 
segmentación por color y aplicaciones donde se desea aislar ciertas áreas de una imagen.
"""
import cv2  # Biblioteca para procesamiento de imágenes
import numpy as np  # Biblioteca para cálculos numéricos

# Lee la imagen desde el archivo "sample_image.jpg"
imagen = cv2.imread('horno3.jpg') 
# Redimensiona la imagen a 320x240 píxeles
imagen = cv2.resize(imagen, (320, 240))

# Convierte la imagen de formato BGR a HSV
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Muestra la imagen original en una ventana llamada "Vista Original"
cv2.imshow('Vista Original', imagen)

# Define un rango de colores para el fondo en el espacio HSV
rango_fondo_min = np.array([110, 110, 110], np.uint8)
rango_fondo_max = np.array([150, 255, 255], np.uint8)

# Define un rango para todos los colores excepto el fondo
rango_excluido_min = np.array([0, 110, 110], np.uint8)
rango_excluido_max = np.array([255, 255, 255], np.uint8)

# Crea una máscara para el fondo usando el rango definido
mascara_fondo = cv2.inRange(imagen_hsv, rango_fondo_min, rango_fondo_max)
# Crea una máscara para seleccionar todo menos el fondo
mascara_invertida = cv2.bitwise_not(mascara_fondo)
# Aplica la máscara para eliminar el fondo de la imagen
imagen_sin_fondo = cv2.bitwise_and(imagen_hsv, imagen_hsv, mask=mascara_invertida)

# Muestra la imagen resultante sin fondo en una ventana llamada "Sin Fondo"
cv2.imshow('Sin Fondo', imagen_sin_fondo)

cv2.waitKey(0)  # Espera hasta que se presione una tecla
cv2.destroyAllWindows()  # Cierra todas las ventanas
