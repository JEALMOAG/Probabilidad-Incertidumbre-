"""
created on 13 April 16:23:56 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código simula el movimiento de puntos aleatorios en un área y utiliza un proceso de re-muestreo para seleccionar
 puntos según su probabilidad basada en la distancia al origen. Este tipo de simulación puede aplicarse en técnicas
 como filtros de partículas o seguimiento de objetos para estimar posiciones con incertidumbre.
"""
import numpy as np  # Biblioteca para cálculos numéricos

# Función para generar puntos aleatorios dentro de un área
def generar_puntos(num_puntos, max_x, max_y):
    return np.random.uniform(low=(0, 0), high=(max_x, max_y), size=(num_puntos, 2))

# Función para medir la distancia (en este ejemplo, solo se mide la distancia al punto de origen)
def calcular_distancia(coordenadas):
    return np.linalg.norm(coordenadas, axis=1)

# Función para realizar un re-muestreo de puntos basándose en las probabilidades de peso
def remuestreo(puntos, probabilidades):
    indices = np.random.choice(len(puntos), size=len(puntos), p=probabilidades)
    return puntos[indices]

# Parámetros del ejemplo
num_puntos = 500  # Número de puntos a generar
limite_area = 15  # Límites para el área de puntos
num_iteraciones = 15  # Número de iteraciones para la simulación

# Generar puntos aleatorios uniformemente distribuidos
puntos = generar_puntos(num_puntos, limite_area, limite_area)

for iteracion in range(num_iteraciones):
    # Simular el movimiento de los puntos (en este ejemplo, agregando ruido gaussiano)
    puntos += np.random.normal(loc=0, scale=0.3, size=puntos.shape)

    # Calcular la distancia desde el origen para cada punto
    distancias = calcular_distancia(puntos)

    # Calcular probabilidades inversamente proporcionales a la distancia
    probabilidades = 1 / distancias
    probabilidades /= np.sum(probabilidades)  # Normalizar las probabilidades

    # Re-muestreo de puntos basado en las probabilidades
    puntos = remuestreo(puntos, probabilidades)

# Estimación final de la posición (promedio de los puntos)
posicion_final = np.mean(puntos, axis=0)

print("Posición final estimada:", posicion_final)


