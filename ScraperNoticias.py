"""El proyecto "Scraper de Noticias con Análisis de Sentimiento" tiene dos 
partes principales:

Scraping de noticias:

Extrae noticias de diferentes fuentes en línea (por ejemplo, periódicos, 
blogs o sitios de noticias).
Puede hacerlo mediante técnicas como requests + BeautifulSoup o utilizando 
Selenium si la web requiere interacción con JavaScript.
Los datos extraídos pueden incluir el título, el contenido, la fecha y el 
enlace de la noticia.
Análisis de Sentimiento:

Analiza el tono emocional de las noticias (positivo, negativo o neutro).
Se puede hacer usando bibliotecas de procesamiento de lenguaje natural como 
TextBlob, VADER (de nltk) o modelos más avanzados con transformers de Hugging Face.
Puede ayudar a identificar tendencias en las noticias, por ejemplo, 
si hay más noticias pesimistas o optimistas sobre un tema."""

import feedparser
import requests
from bs4 import BeautifulSoup

# URL del feed RSS de BBC Mundo
rss_url = 'http://feeds.bbci.co.uk/mundo/rss.xml'

# Parsear el feed
feed = feedparser.parse(rss_url)

# Función para obtener el contenido de un artículo
def obtener_contenido(url):
    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        
        # Encontrar el contenido principal del artículo
        cuerpo = soup.find_all('p')
        texto = '\n'.join([p.get_text() for p in cuerpo])
        
        return texto.strip()
    except Exception as e:
        return f"Error al obtener el contenido: {e}"

# Iterar sobre las noticias y obtener su contenido
for entry in feed.entries[:5]:  # Solo las primeras 5 noticias para prueba
    print(f"Título: {entry.title}")
    print(f"Enlace: {entry.link}")
    print("Contenido:")
    print(obtener_contenido(entry.link))
    print("-" * 80)

