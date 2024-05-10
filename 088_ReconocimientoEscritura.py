"""
created on 12 Abril 23:12:03 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código realiza OCR en una imagen para identificar y extraer texto, mostrando tanto el texto detectado como la
 imagen procesada. Se utiliza para obtener texto a partir de imágenes y podría aplicarse en escenarios como digitalización
 de documentos, procesamiento de imágenes con texto, o extracción de información visual.
"""
import easyocr  # Biblioteca para OCR
from PIL import Image  # Biblioteca para manejo de imágenes

# Crear un objeto de EasyOCR para el reconocimiento de texto en español
lector = easyocr.Reader(['es'])

# Cargar una imagen desde un archivo
foto = Image.open('text.png')

# Redimensionar la imagen si es demasiado grande
ancho, alto = foto.size
if ancho > 800 or alto > 800:
    foto = foto.resize((ancho // 2, alto // 2))  # Redimensionar a la mitad

# Realizar OCR en la imagen para extraer texto
resultado = lector.readtext(foto)

# Iterar sobre los resultados para extraer el texto detectado
for deteccion in resultado:
    texto = deteccion[1]
    print('Texto encontrado: "{}"'.format(texto))  # Imprimir el texto detectado

# Mostrar la imagen con el texto resaltado
foto.show()  # Mostrar la imagen
