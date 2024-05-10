"""
created on 12 Abril 07:25:09 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código crea un traductor básico de inglés a español usando etiquetado 
de partes del discurso y probabilidades de palabras. Tokeniza y etiqueta 
las frases de entrenamiento, calcula probabilidades de traducción y luego 
traduce nuevas frases utilizando estas probabilidades. Finalmente, imprime 
la traducción de una frase de ejemplo.
"""
import nltk  # Librería para procesamiento de lenguaje natural
import numpy as np  # Librería para cálculos numéricos

# Descargar recursos de NLTK
nltk.download('punkt')  # Descarga para tokenización
nltk.download('averaged_perceptron_tagger')  # Descarga para etiquetado POS

# Frases de entrenamiento en dos idiomas
frases_ing = [
    "a mouse",
    "a rabbit",
    "a fox",
    "the fox",
    "the mouse",
    "with"
]

frases_esp = [
    "un ratón",
    "un conejo",
    "un zorro",
    "el zorro",
    "el ratón",
    "con"
]

# Tokenización y etiquetado POS
tokens_ing = [nltk.word_tokenize(frase) for frase in frases_ing]  # Tokeniza frases en inglés
tokens_esp = [nltk.word_tokenize(frase) for frase in frases_esp]  # Tokeniza frases en español

etiquetado_ing = [nltk.pos_tag(tokens) for tokens in tokens_ing]  # Etiqueta POS en inglés
etiquetado_esp = [nltk.pos_tag(tokens) for tokens in tokens_esp]  # Etiqueta POS en español

# Crear conjuntos de palabras y etiquetas POS
palabras_ing = set(palabra for lista in tokens_ing for palabra in lista)  # Palabras en inglés
palabras_esp = set(palabra for lista in tokens_esp for palabra in lista)  # Palabras en español

etiquetas_ing = set(etiqueta for lista in etiquetado_ing for _, etiqueta in lista)  # Etiquetas POS en inglés
etiquetas_esp = set(etiqueta for lista in etiquetado_esp for _, etiqueta in lista)  # Etiquetas POS en español

# Crear matriz de probabilidades de traducción
matriz_prob = np.zeros((len(palabras_ing), len(palabras_esp)))  # Crea una matriz de ceros

# Calcular frecuencias de traducción
for lista_ing, lista_esp in zip(etiquetado_ing, etiquetado_esp):  # Recorre las frases etiquetadas
    for (pal_ing, etq_ing), (pal_esp, etq_esp) in zip(lista_ing, lista_esp):  # Recorre las palabras etiquetadas
        ind_ing = list(palabras_ing).index(pal_ing)  # Índice de la palabra en inglés
        ind_esp = list(palabras_esp).index(pal_esp)  # Índice de la palabra en español
        matriz_prob[ind_ing, ind_esp] += 1  # Incrementa la cuenta de traducción

# Normalizar probabilidades
matriz_prob /= matriz_prob.sum(axis=1, keepdims=True)  # Normaliza las probabilidades de traducción

# Crear un diccionario para mapear palabras en inglés a índices en la matriz de probabilidades
indice_palabras_ing = {palabra: indice for indice, palabra in enumerate(palabras_ing)}

# Función para traducir una frase de inglés a español
def traducir(oracion):
    tokens = nltk.word_tokenize(oracion)  # Tokeniza la frase
    etiquetado = nltk.pos_tag(tokens)  # Etiqueta POS
    resultado = []  # Lista para la traducción

    for palabra, etiqueta in etiquetado:  # Recorre la frase etiquetada
        if palabra in indice_palabras_ing:  # Verifica si la palabra está en el diccionario
            ind_ing = indice_palabras_ing[palabra]  # Índice de la palabra en inglés
            ind_esp = np.argmax(matriz_prob[ind_ing])  # Índice de la traducción más probable
            resultado.append(list(palabras_esp)[ind_esp])  # Agrega la palabra traducida

    return " ".join(resultado)  # Devuelve la frase traducida

# Ejemplo de uso
oracion_entrada = "a rabbit and a fox"  # Nueva frase de entrada
oracion_salida = traducir(oracion_entrada)  # Traducción
print("Entrada:", oracion_entrada)  # Imprime la frase de entrada
print("Traducida:", oracion_salida)  # Imprime la traducción
