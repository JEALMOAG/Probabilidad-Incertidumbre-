"""
created on 13 April 13:25:14 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código simula un proceso de control de temperatura con un sensor y un actuador ficticios. 
A través de un bucle, se mide la temperatura y se toman decisiones para ajustar la calefacción, demostrando un mecanismo 
simple para la automatización basada en sensores y actuadores.
"""
import time  # Para pausas en la ejecución
import random  # Para generación de valores aleatorios

# Clase para simular un sensor de temperatura ficticio
class SensorTemperatura:
    def __init__(self):  # Constructor de la clase
        pass  # No se realiza ninguna acción en el constructor

    def medir_temperatura(self):  # Método para simular la medición de temperatura
        # Simular lectura de temperatura
        return random.randint(15, 35)  # Retorna un valor aleatorio entre 15 y 35 grados Celsius

# Clase para simular un actuador de calefacción ficticio
class Calefaccion:
    def __init__(self):  # Constructor de la clase
        pass  # El constructor no realiza acciones específicas

    def ajustar(self, accion):  # Método para simular ajuste de calefacción
        # Simular ajuste de la calefacción
        print(f'Calefacción ajustada para {accion}')  # Imprime la acción realizada

# Función para simular el control de temperatura
def controlar_temperatura(sensor, actuador, ajustes=7):  # Función principal para control de temperatura
    ajustes_realizados = 0  # Inicializa el contador de ajustes
    while ajustes_realizados < ajustes:  # Bucle para controlar los ajustes
        # Leer la temperatura del sensor
        temperatura = sensor.medir_temperatura()  # Llamada al método para medir la temperatura
        print(f'Temperatura medida: {temperatura} grados')  # Imprime la temperatura medida

        # Ajustar la calefacción según la temperatura
        if temperatura < 22:  # Si la temperatura es menor que 22 grados Celsius
            actuador.ajustar('aumentar temperatura')  # Ajusta la calefacción para aumentar la temperatura
        else:  # Si la temperatura es 22 grados o más
            actuador.ajustar('disminuir temperatura')  # Ajusta la calefacción para disminuir la temperatura

        ajustes_realizados += 1  # Incrementa el contador de ajustes

        time.sleep(1)  # Pausa por 1 segundo entre cada ajuste

# Crear instancias del sensor de temperatura y del actuador de calefacción
sensor_temperatura = SensorTemperatura()  # Crea el sensor de temperatura
calefaccion = Calefaccion()  # Crea el actuador de calefacción

# Simular el control de temperatura con 7 ajustes
controlar_temperatura(sensor_temperatura, calefaccion, ajustes=7)  # Llama a la función para simular el control de temperatura
