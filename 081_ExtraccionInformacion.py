"""
created on 11 Abril 23:45:12 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
 El código analiza un texto, limpiando datos no relevantes y determinando 
 las palabras más comunes.
 Esta información es útil para el análisis de texto y tareas relacionadas 
 con el procesamiento del lenguaje natural.

"""
# Importación de bibliotecas de NLTK
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist

# Descarga de recursos necesarios para tokenización y stopwords en español
nltk.download('punkt')
nltk.download('stopwords')

# Definición del texto de ejemplo
mensaje = "Los gatos son animales fascinantes. Su agilidad y elegancia los hacen muy queridos por muchas personas."

# Tokenización del texto en palabras
palabras = word_tokenize(mensaje.lower())

# Creación de un conjunto de stopwords en español
palabras_prohibidas = set(stopwords.words('spanish'))

# Filtrado de stopwords y eliminación de caracteres no alfanuméricos
palabras_filtradas = [palabra for palabra in palabras if palabra.isalnum() and palabra not in palabras_prohibidas]

# Inicialización del objeto Stemmer para aplicar stemming
raizador = PorterStemmer()

# Aplicación de stemming a las palabras filtradas
palabras_rai = [raizador.stem(palabra) for palabra in palabras_filtradas]

# Cálculo de la frecuencia de cada palabra
dist_frecuencia = FreqDist(palabras_rai)

# Impresión de las 5 palabras más frecuentes
print(dist_frecuencia.most_common(5))
