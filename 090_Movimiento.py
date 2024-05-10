"""
created on 13 April 10:45:18 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código muestra cómo simular el movimiento de un objeto en una matriz, desplazándolo hacia la derecha en cada paso,
 y muestra el estado actualizado en la consola. El código es útil para entender conceptos básicos de simulación y 
animación, además de ilustrar la manipulación de matrices y el control del tiempo.
"""
import numpy as np  # Importar biblioteca para matrices y operaciones numéricas
import time  # Biblioteca para gestión de tiempo

# Función para imprimir la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(' '.join(fila))  # Imprime la matriz fila por fila

# Función para simular el movimiento en la matriz
def simular_desplazamiento(matriz):
    # Crear nueva matriz para el siguiente paso
    nueva_matriz = np.full_like(matriz, ' ')  # Rellena con espacios vacíos
    
    # Iterar sobre cada celda de la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            # Simular movimiento de un objeto
            # Mover un objeto representado por 'O' hacia la derecha
            if matriz[i][j] == 'O':
                nueva_posicion = (i, j + 1)  # Nueva posición a la derecha
                # Verificar si la nueva posición está dentro de los límites
                if 0 <= nueva_posicion[1] < len(matriz[0]):
                    nueva_matriz[nueva_posicion] = 'O'
    
    return nueva_matriz  # Retornar la nueva matriz con el movimiento simulado

# Definir tamaño de la matriz
alto = 6
largo = 12

# Crear matriz inicial con un objeto 'O'
matriz = np.full((alto, largo), ' ')  # Rellenar con espacios
matriz[3][3] = 'O'  # Colocar un objeto en la posición inicial

# Simular el desplazamiento del objeto en la matriz
for _ in range(6):
    imprimir_matriz(matriz)  # Imprimir el estado actual de la matriz
    print('-' * (largo * 2))  # Separador para cada paso
    matriz = simular_desplazamiento(matriz)  # Simular el desplazamiento
    time.sleep(1)  # Esperar un segundo entre pasos
