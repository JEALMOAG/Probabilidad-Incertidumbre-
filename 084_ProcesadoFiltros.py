"""
created on 12 Abril 13:28:05 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código aplica un filtro de color a una imagen para resaltar áreas específicas, mostrándolas visualmente.
Esta técnica es útil para tareas de procesamiento de imágenes como detección de objetos basados en colores.
"""
import cv2
import numpy as np

# Leer una imagen y cambiar su tamaño
imagen = cv2.imread('horno3.jpg')
imagen = cv2.resize(imagen, (320, 240))

# Crear una imagen de fondo amarillo del mismo tamaño que la imagen original
fondo_amarillo = np.full_like(imagen, (0, 255, 255), dtype=np.uint8)  # Amarillo en formato BGR

# Superponer la imagen original sobre el fondo amarillo
imagen_con_fondo_amarillo = cv2.addWeighted(fondo_amarillo, 1, imagen, 1, 0)

# Mostrar la imagen con fondo amarillo
cv2.imshow('Imagen con Fondo Amarillo', imagen_con_fondo_amarillo)

# Definir límites para la detección de color (ejemplo para el rango amarillo)
limite_inferior = np.array([25, 100, 100], np.uint8)
limite_superior = np.array([35, 255, 255], np.uint8)

# Convertir la imagen a espacio de color HSV
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Crear una máscara que muestre solo el rango de color amarillo
mascara_amarillo = cv2.inRange(imagen_hsv, limite_inferior, limite_superior)

# Mostrar la máscara de color amarillo
cv2.imshow('Filtro Amarillo', mascara_amarillo)
cv2.imwrite("horno3FAmarillo.jpg", mascara_amarillo)
# Esperar por una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
