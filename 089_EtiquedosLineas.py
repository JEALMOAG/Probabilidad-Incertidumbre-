"""
created on 13 April 06:21:56 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código contiene una función que puede identificar la orientación de líneas en matrices de píxeles.
 Luego, la función se prueba con matrices de ejemplo para validar su precisión, mostrando si las líneas
 son horizontales o verticales. Este tipo de funcionalidad es útil para procesamiento de imágenes y aplicaciones
 relacionadas con detección de estructuras o patrones.
"""
import numpy as np  # Biblioteca para operaciones con matrices

# Función para determinar si una línea es horizontal o vertical
def identificar_orientacion(matriz):
    # Toma una matriz como entrada y determina la orientación de una línea
    
    alto, ancho = matriz.shape
    # Obtiene las dimensiones de la matriz

    # Suma de valores a lo largo de filas y columnas
    suma_por_fila = np.sum(matriz, axis=1)
    suma_por_columna = np.sum(matriz, axis=0)
    # Suma de valores por fila y por columna

    # Determina si la línea es horizontal o vertical
    if np.mean(suma_por_fila) > np.mean(suma_por_columna):
        return "horizontal"
    else:
        return "vertical"
    # Retorna la orientación de la línea según la media de las sumas por filas y columnas

# Ejemplo de matriz con línea horizontal
matriz_horizontal = np.array([[0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0]])
# Definición de una matriz con una línea horizontal

# Ejemplo de matriz con línea vertical
matriz_vertical = np.array([[0, 1, 0, 0, 0],
                            [0, 1, 0, 0, 0],
                            [0, 1, 0, 0, 0],
                            [0, 1, 0, 0, 0],
                            [0, 1, 0, 0, 0]])
# Definición de una matriz con una línea vertical

# Probar la función de orientación
resultado_h = identificar_orientacion(matriz_horizontal)
resultado_v = identificar_orientacion(matriz_vertical)
# Llamadas a la función para probar con ejemplos

# Imprimir resultados
print("La orientación de la línea en la matriz horizontal es:", resultado_h)
print("La orientación de la línea en la matriz vertical es:", resultado_v)
# Imprimir resultados para comprobar la orientación de las líneas
