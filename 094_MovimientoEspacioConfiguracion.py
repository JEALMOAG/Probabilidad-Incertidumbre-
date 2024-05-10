"""
created on 13 April 21:02:15 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código busca un camino dentro de un área con obstáculos usando búsqueda en anchura, explorando sistemáticamente
 celdas adyacentes para encontrar la ruta más corta entre un punto de inicio y un destino. El uso de BFS garantiza 
que el primer camino encontrado sea el más corto posible.
"""
import numpy as np  # Para operaciones numéricas
from collections import deque  # Para estructuras de cola eficientes

# Clase para definir un área con obstáculos
class Area:
    def __init__(self, ancho, alto, barreras):
        self.ancho = ancho  # Ancho del área
        self.alto = alto  # Alto del área
        self.barreras = barreras  # Lista de coordenadas con barreras

    # Función para verificar si una coordenada está libre y dentro del área
    def es_espacio_libre(self, coordenada):
        x, y = coordenada
        return 0 <= x < self.ancho and 0 <= y < self.alto and (x, y) not in self.barreras

# Función para encontrar un camino desde el inicio hasta el destino usando búsqueda en anchura
def buscar_ruta(area, inicio, destino):
    # Inicialización de la búsqueda
    visitados = set()  # Conjunto de celdas ya visitadas
    cola = deque([(inicio, [])])  # Cola para búsqueda en anchura, almacenando la ruta

    # Búsqueda en anchura
    while cola:
        celda_actual, ruta_actual = cola.popleft()  # Obtener la celda actual y la ruta hasta ella
        if celda_actual == destino:  # Si la celda actual es el destino, devolver la ruta
            return ruta_actual + [celda_actual]
        if celda_actual in visitados:  # Si ya ha sido visitada, continuar con la siguiente
            continue
        visitados.add(celda_actual)  # Marcar como visitada
        # Coordenadas de celdas adyacentes
        adyacentes = [(celda_actual[0] + dx, celda_actual[1] + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
        # Filtrar celdas adyacentes que están libres y dentro del área
        adyacentes_libres = [c for c in adyacentes if area.es_espacio_libre(c)]
        # Agregar las celdas adyacentes a la cola con la ruta actual más la nueva celda
        for celda in adyacentes_libres:
            cola.append((celda, ruta_actual + [celda]))

    # Si no se encuentra un camino, devolver None
    return None

# Definición del área (tamaño: 12x12, barreras en las posiciones (2, 3), (3, 3), y (4, 3))
area = Area(12, 12, [(2, 3), (3, 3), (4, 3)])

# Punto de inicio y destino
origen = (0, 0)
destino = (10, 10)

# Buscar la ruta desde el origen hasta el destino
ruta = buscar_ruta(area, origen, destino)

# Imprimir la ruta encontrada
if ruta:
    print("Ruta encontrada:", ruta)
else:
    print("No se pudo encontrar una ruta.")
    