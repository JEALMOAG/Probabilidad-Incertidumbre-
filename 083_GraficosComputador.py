"""
created on 12 Abril 11:00:45 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código utiliza la biblioteca `speech_recognition` para reconocer comandos de
 voz y controlar la creación de gráficos en una ventana de Pygame. Después de
 inicializar Pygame y definir funciones para dibujar un círculo y un cuadrado,
 la función principal espera comandos de voz del usuario. Cuando se reconoce un 
 comando ("círculo" o "cuadrado"), se dibuja el objeto correspondiente en la
 ventana de Pygame. El programa maneja posibles errores de reconocimiento de 
 voz y se cierra adecuadamente cuando se sale del bucle principal.
"""
# Importar las bibliotecas necesarias
import speech_recognition as sr  # Biblioteca para el reconocimiento de voz
import pygame  # Biblioteca para la creación de gráficos por computadora

# Inicializar Pygame
pygame.init()  # Inicializar Pygame
pantalla = pygame.display.set_mode((640, 480))  # Crear una ventana de 640x480 píxeles
pygame.display.set_caption('Gráficos por Reconocimiento de Voz')  # Establecer el título de la ventana

# Función para dibujar un círculo
def dibujar_circulo(x, y):
    pygame.draw.circle(pantalla, (0, 0, 255), (x, y), 30)  # Dibujar un círculo azul en la posición especificada

# Función para dibujar un cuadrado
def dibujar_cuadrado(x, y):
    pygame.draw.rect(pantalla, (255, 255, 0), pygame.Rect(x - 30, y - 30, 60, 60))  # Dibujar un cuadrado amarillo en la posición especificada

# Función principal
def ejecutar_programa():
    reconocedor = sr.Recognizer()  # Crear un objeto para el reconocimiento de voz
    comando_reconocido = False  # Bandera para indicar si se ha reconocido un comando

    activo = True  # Bandera para indicar si el programa está en ejecución
    while activo:  # Bucle principal del programa
        for evento in pygame.event.get():  # Iterar sobre los eventos de pygame
            if evento.type == pygame.QUIT:  # Si se presiona el botón de cierre de la ventana
                activo = False  # Detener el bucle principal

        if not comando_reconocido:  # Si no se ha reconocido un comando
            with sr.Microphone() as fuente:  # Abrir el micrófono
                print("Por favor, diga un comando ('círculo' o 'cuadrado'):")  # Solicitar al usuario un comando
                audio = reconocedor.listen(fuente)  # Escuchar el audio del micrófono

            try:  # Intentar reconocer el comando
                comando = reconocedor.recognize_google(audio, language="es-ES")  # Reconocer el comando usando Google Speech Recognition
                print("Comando reconocido:", comando)  # Mostrar el comando reconocido

                if "círculo" in comando:  # Si el comando es "círculo"
                    dibujar_circulo(320, 240)  # Dibujar un círculo en el centro de la pantalla
                elif "cuadrado" in comando:  # Si el comando es "cuadrado"
                    dibujar_cuadrado(320, 240)  # Dibujar un cuadrado en el centro de la pantalla
                else:  # Si el comando no es reconocido
                    print("Comando no reconocido")  # Mostrar un mensaje indicando que el comando no fue reconocido
                
                pygame.display.flip()  # Actualizar la pantalla
                comando_reconocido = True  # Marcar que el comando fue reconocido

            except sr.UnknownValueError:  # Si el audio no puede ser entendido
                print("No se pudo entender el audio")  # Mostrar un mensaje de error
            except sr.RequestError as e:  # Si hay un problema con la solicitud
                print("Error en la solicitud: {0}".format(e))  # Mostrar el error detallado

    pygame.quit()  # Cerrar Pygame

if __name__ == "__main__":  # Si este script es el programa principal
    ejecutar_programa()  # Llamar a la función principal
