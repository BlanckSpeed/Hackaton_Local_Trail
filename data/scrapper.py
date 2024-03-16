import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página que contiene la lista de tiendas
url = 'https://www.guiarepsol.com/es/viajar/nos-gusta/mas-que-local-pequeno-comercio-en-el-centro-de-madrid/'

# Realizar la petición HTTP a la página web
respuesta = requests.get(url)

# Analizar el contenido HTML de la página
soup = BeautifulSoup(respuesta.text, 'html.parser')

# Encontrar los elementos que contienen la información de las tiendas
# Deberás identificar los selectores correctos que contienen los nombres de las tiendas y sus descripciones
elementos_tiendas = soup.find_all('tu_selector_para_elementos_de_tienda')

# Lista para almacenar la información extraída
tiendas_info = []

# Extraer la información de cada tienda
for elemento in elementos_tiendas:
    # Extraer el nombre de la tienda
    nombre_tienda = elemento.find('tu_selector_para_nombre_de_tienda').get_text(strip=True)
    
    # Extraer la descripción de la tienda
    descripcion_tienda = elemento.find('tu_selector_para_descripcion_de_tienda').get_text(strip=True)
    
    # Extraer la ubicación y el tipo de tienda de la descripción
    # Esto puede requerir procesamiento adicional dependiendo de la estructura de la descripción
    ubicacion_tipo = descripcion_tienda.split(':')
    ubicacion = ubicacion_tipo[0].strip()
    tipo_tienda = ubicacion_tipo[1].strip() if len(ubicacion_tipo) > 1 else 'Tipo no especificado'
    
    # Agregar la información a la lista
    tiendas_info.append({
        'Tienda': nombre_tienda,
        'Ubicación': ubicacion,
        'Tipo de Tienda': tipo_tienda
    })

# Crear un DataFrame con los datos extraídos
data = pd.DataFrame(tiendas_info)

# Guardar el DataFrame en un archivo CSV
data.to_csv('tiendas_madrid.csv', index=False)

print('Scraper completado y DataFrame guardado como tiendas_madrid.csv')