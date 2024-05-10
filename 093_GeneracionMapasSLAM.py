"""
created on 13 April 13:25:14 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código simula el movimiento y re-muestreo de puntos aleatorios en un área definida y muestra la trayectoria
 estimada mediante visualización gráfica. El re-muestreo basado en probabilidades y el cálculo de distancias
 permiten simular un filtro de partículas, una técnica utilizada para seguimiento y estimación de posiciones en
 entornos con incertidumbre.
"""
import numpy as np  # Librería para operaciones numéricas
import matplotlib.pyplot as plt  # Para visualización de datos

# Parámetros de la simulación
num_puntos = 800  # Número de puntos para el filtro
limite_area = 15  # Límite del área (cuadrado de 15x15)
num_iteraciones = 25  # Número de pasos en la simulación

# Función para generar puntos aleatorios dentro del área definida
def generar_puntos(num_puntos, max_x, max_y):
    return np.random.uniform(low=(0, 0), high=(max_x, max_y), size=(num_puntos, 2))

# Función para calcular distancia (usando la distancia al origen)
def calcular_distancia(coordenadas):
    return np.linalg.norm(coordenadas, axis=1)

# Función para re-muestrear puntos basándose en probabilidades de peso
def remuestreo_puntos(puntos, probabilidades):
    indices = np.random.choice(len(puntos), size=len(puntos), p=probabilidades)
    return puntos[indices]

# Función para visualizar el área y la trayectoria estimada
def visualizar_area(puntos, ruta, puntos_reales=None):
    plt.figure(figsize=(10, 8))  # Tamaño de la gráfica
    plt.scatter(puntos[:, 0], puntos[:, 1], color='b', s=6, alpha=0.5)  # Puntos en azul
    plt.plot(ruta[:, 0], ruta[:, 1], color='r', linewidth=2)  # Trajectoria estimada en rojo
    if puntos_reales is not None:
        plt.scatter(puntos_reales[:, 0], puntos_reales[:, 1], color='g', s=25, marker='x')  # Puntos reales en verde
    plt.xlabel('Coordenada X')  # Etiqueta para el eje X
    plt.ylabel('Coordenada Y')  # Etiqueta para el eje Y
    plt.title('Área y trayectoria estimada')  # Título de la gráfica
    plt.grid(True)  # Habilita la cuadrícula
    plt.axis('equal')  # Configura los ejes para que tengan la misma escala
    plt.show()  # Mostrar la gráfica

# Inicialización: Generar puntos aleatorios uniformemente distribuidos en el área
puntos = generar_puntos(num_puntos, limite_area, limite_area)

# Inicializar la trayectoria estimada
ruta = np.zeros((num_iteraciones, 2))

for paso in range(num_iteraciones):
    # Simulación del movimiento (ruido gaussiano en los puntos)
    puntos += np.random.normal(loc=0, scale=0.4, size=puntos.shape)

    # Medición: Calcular distancia desde el origen
    distancias = calcular_distancia(puntos)

    # Calcular probabilidades basadas en las distancias (inversa de la distancia)
    probabilidades = 1 / distancias
    probabilidades /= np.sum(probabilidades)  # Normalizar probabilidades

    # Re-muestreo de puntos basado en probabilidades
    puntos = remuestreo_puntos(puntos, probabilidades)

    # Actualizar la trayectoria estimada (promedio de los puntos)
    ruta[paso] = np.mean(puntos, axis=0)

# Visualizar el área y la trayectoria estimada
visualizar_area(puntos, ruta)


