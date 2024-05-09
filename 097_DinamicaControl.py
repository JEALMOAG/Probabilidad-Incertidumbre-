"""
created on 13 Abril 08:12:45 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
Este código simula el control de un péndulo utilizando un controlador
proporcional-derivativo (PD). Primero define la función de control PD,
luego establece los parámetros del péndulo y del controlador.
A continuación, simula el comportamiento del péndulo bajo la influencia del
control PD a lo largo del tiempo, utilizando integración numérica para
actualizar el estado del péndulo. Finalmente, visualiza los resultados en
gráficos que muestran el ángulo y la velocidad angular del péndulo en función
del tiempo.
"""
import numpy as np  # Importa la librería NumPy para operaciones numéricas
import matplotlib.pyplot as plt  # Importa la librería Matplotlib para visualización

# Definición de la función de control PD
def control_pd(ángulo, velocidad_angular, Kp, Kd):
    # Calcula la señal de control como la suma de la componente proporcional y derivativa
    return Kp * ángulo + Kd * velocidad_angular

# Parámetros del péndulo
m = 1  # Masa del péndulo
l = 1  # Longitud del péndulo
g = 9.81  # Aceleración debido a la gravedad

# Parámetros del control PD
Kp = 20  # Ganancia proporcional
Kd = 5  # Ganancia derivativa

# Condiciones iniciales
ángulo_0 = np.pi / 4  # Ángulo inicial del péndulo
velocidad_angular_0 = 0  # Velocidad angular inicial del péndulo

# Tiempo de simulación
dt = 0.01  # Paso de tiempo
t_simulación = np.arange(0, 5, dt)  # Vector de tiempo

# Inicialización de variables
ángulo = ángulo_0  # Ángulo inicial del péndulo
velocidad_angular = velocidad_angular_0  # Velocidad angular inicial del péndulo
ángulo_hist = []  # Historial de ángulos del péndulo
velocidad_angular_hist = []  # Historial de velocidades angulares del péndulo
u_hist = []  # Historial de señales de control

# Simulación del control del péndulo
for t in t_simulación:
    # Almacena los valores actuales de ángulo y velocidad angular
    ángulo_hist.append(ángulo)
    velocidad_angular_hist.append(velocidad_angular)
    
    # Calcula la señal de control utilizando el control PD
    u = control_pd(ángulo, velocidad_angular, Kp, Kd)
    u_hist.append(u)
    
    # Calcula la aceleración angular utilizando el modelo dinámico del péndulo
    aceleración_angular = (-g / l) * np.sin(ángulo) + u / (m * l**2)
    
    # Actualiza el ángulo y la velocidad angular utilizando la integración numérica
    ángulo += velocidad_angular * dt
    velocidad_angular += aceleración_angular * dt

# Visualización de los resultados
plt.figure(figsize=(10, 6))

# Graficar el ángulo del péndulo en función del tiempo
plt.subplot(2, 1, 1)
plt.plot(t_simulación, np.rad2deg(ángulo_hist), label='Ángulo (grados)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Ángulo (grados)')
plt.legend()

# Graficar la velocidad angular del péndulo en función del tiempo
plt.subplot(2, 1, 2)
plt.plot(t_simulación, np.rad2deg(velocidad_angular_hist), label='Velocidad Angular (grados/s)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad Angular (grados/s)')
plt.legend()

plt.tight_layout()
plt.show()
