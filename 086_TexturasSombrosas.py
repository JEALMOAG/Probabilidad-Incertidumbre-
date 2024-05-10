"""
created on 12 Abril 20:32:19 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código carga una imagen, la convierte a HSV y muestra ambas versiones para visualización. 
Esta estructura es útil para aplicar diferentes procesos de análisis de imágenes y examinar resultados.
"""
import cv2  # Importa la librería OpenCV para procesamiento de imágenes
import numpy as np  # Importa la librería NumPy para operaciones numéricas

# Cargar la imagen desde el archivo "example_image.jpg"
imagen = cv2.imread('horno3.jpg')  
# Redimensionar la imagen a 320x240 píxeles
imagen = cv2.resize(imagen, (320, 240))  
# Convertir la imagen de formato BGR a HSV
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)  

# Mostrar la imagen original en una ventana llamada "Vista Original"
cv2.imshow('Vista Original', imagen)  
# Mostrar la imagen convertida a HSV en una ventana llamada "HSV Visualización"
cv2.imshow('HSV Visualización', imagen_hsv)  

cv2.waitKey(0)  # Esperar hasta que se presione una tecla
cv2.destroyAllWindows()  # Cerrar todas las ventanas de visualización
