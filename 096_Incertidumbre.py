"""
created on 13 Abril 05:34:07 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
Este código implementa un filtro de Kalman extendido (EKF) para estimar el
estado de un sistema dinámico a partir de mediciones ruidosas. El filtro de
Kalman extendido es una extensión del filtro de Kalman clásico que permite
modelar sistemas no lineales. El código incluye funciones para la predicción
del estado futuro y la actualización del estado basada en las mediciones
actuales. Se aplican estas funciones iterativamente a cada medición para
estimar el estado del sistema a lo largo del tiempo.
"""
import numpy as np  # Importa la librería NumPy para operaciones numéricas

# Definición de la función de predicción del filtro de Kalman extendido (EKF)
def predecir_estado(estado_actual, covarianza_actual, matriz_transicion, covarianza_proceso):
    estado_predicho = np.dot(matriz_transicion, estado_actual)  # Predice el nuevo estado utilizando la matriz de transición de estado
    covarianza_predicha = np.dot(matriz_transicion, np.dot(covarianza_actual, matriz_transicion.T)) + covarianza_proceso  # Predice la nueva covarianza del estado
    return estado_predicho, covarianza_predicha

# Definición de la función de actualización del filtro de Kalman extendido (EKF)
def actualizar_estado(estado_predicho, covarianza_predicha, medicion, matriz_observacion, covarianza_medicion):
    innovacion = medicion - np.dot(matriz_observacion, estado_predicho)  # Calcula la innovación entre la medición y la predicción
    matriz_innovacion = np.dot(matriz_observacion, np.dot(covarianza_predicha, matriz_observacion.T)) + covarianza_medicion  # Calcula la matriz de covarianza de la innovación
    ganancia_kalman = np.dot(covarianza_predicha, np.dot(matriz_observacion.T, np.linalg.inv(matriz_innovacion)))  # Calcula la ganancia de Kalman
    estado_actualizado = estado_predicho + np.dot(ganancia_kalman, innovacion)  # Actualiza el estado estimado
    covarianza_actualizada = covarianza_predicha - np.dot(ganancia_kalman, np.dot(matriz_observacion, covarianza_predicha))  # Actualiza la covarianza del estado
    return estado_actualizado, covarianza_actualizada

# Parámetros del filtro de Kalman extendido (EKF)
delta_t = 0.1  # Intervalo de tiempo entre cada actualización
matriz_transicion = np.array([[1, delta_t], [0, 1]])  # Matriz de transición de estado (modelo dinámico del sistema)
matriz_observacion = np.array([[1, 0]])  # Matriz de observación (relaciona el estado con las observaciones)
covarianza_proceso = np.array([[0.1, 0], [0, 0.01]])  # Covarianza del proceso (incertidumbre del modelo)
covarianza_medicion = np.array([[1]])  # Covarianza de la medición (incertidumbre de las observaciones)

# Condiciones iniciales del filtro de Kalman extendido (EKF)
estado_inicial = np.array([0, 0])  # Estado inicial (posición y velocidad)
covarianza_inicial = np.array([[1, 0], [0, 1]])  # Covarianza inicial del estado

# Datos de la medición (en este ejemplo, solo se proporciona la posición)
mediciones = [1, 2, 3, 4, 5]

# Inicialización de las listas para almacenar los resultados
resultados_estado = []
resultados_covarianza = []

# Aplicar el filtro de Kalman extendido (EKF) para cada medición
for medicion in mediciones:
    # Predicción del estado siguiente
    estado_predicho, covarianza_predicha = predecir_estado(estado_inicial, covarianza_inicial, matriz_transicion, covarianza_proceso)
    
    # Actualización del estado basada en la medición
    estado_actualizado, covarianza_actualizada = actualizar_estado(estado_predicho, covarianza_predicha, medicion, matriz_observacion, covarianza_medicion)
    
    # Almacenar los resultados de la estimación del estado y la covarianza
    resultados_estado.append(estado_actualizado)
    resultados_covarianza.append(covarianza_actualizada)

# Imprimir los resultados de la estimación
for i in range(len(mediciones)):
    print("Medición:", mediciones[i])
    print("Estado estimado:", resultados_estado[i])
    print("Covarianza del estado:", resultados_covarianza[i])
    print()
