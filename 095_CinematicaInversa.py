"""
created on 13 Abril 23:34:05 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código calcula los ángulos necesarios de las articulaciones de un robot de
2DOF para alcanzar una posición específica en un plano cartesiano. Utiliza la
cinemática inversa y conceptos trigonométricos para este cálculo.
Los resultados se proporcionan en grados.
"""
import numpy as np  # Importa la librería NumPy para operaciones numéricas

# Definición de la función para calcular la cinemática inversa del robot de 2DOF
def cinemática_inversa(x, y, L1, L2):
    # Calcula la distancia desde el origen al punto objetivo utilizando el teorema de Pitágoras
    distancia = np.sqrt(x**2 + y**2)
    
    # Calcula el ángulo entre el segmento L1 y la línea que conecta el origen con el punto objetivo
    beta = np.arccos((L1**2 + distancia**2 - L2**2) / (2 * L1 * distancia))
    
    # Calcula el ángulo entre el segmento L2 y la línea que conecta el punto objetivo con el segmento L1
    gamma = np.arctan2(y, x)  # Usamos la función arctan2 para manejar todos los cuadrantes
    
    # Calcula el ángulo de la articulación 1 restando beta de gamma
    theta1 = gamma - beta
    
    # Calcula el ángulo de la articulación 2 utilizando la ley de los cosenos
    theta2 = np.arccos((L1**2 + L2**2 - distancia**2) / (2 * L1 * L2))
    
    return np.degrees(theta1), np.degrees(theta2)  # Convierte los ángulos a grados y los devuelve

# Dimensiones del robot (longitudes de los eslabones)
longitud_eslabón1 = 5  # Longitud del primer eslabón
longitud_eslabón2 = 4  # Longitud del segundo eslabón

# Posición objetivo en el espacio cartesiano
x_objetivo = 2
y_objetivo = 3

# Calcula los ángulos de las articulaciones necesarios para alcanzar la posición objetivo
ángulo_articulación1, ángulo_articulación2 = cinemática_inversa(x_objetivo, y_objetivo, longitud_eslabón1, longitud_eslabón2)

# Imprime los ángulos calculados
print("Ángulo de la articulación 1:", ángulo_articulación1, "grados")
print("Ángulo de la articulación 2:", ángulo_articulación2, "grados")
