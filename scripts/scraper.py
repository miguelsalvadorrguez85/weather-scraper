import requests
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import os

# URL de la estación de Gijón en Meteoclimatic
URL = 'https://www.meteoclimatic.net/perfil/ESAST3300000033010A'  # cambia por tu URL exacta

# Hacer la petición
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# EXTRAER LOS DATOS (esto lo tendrás que adaptar un poco según el HTML real)
# Ejemplo muy simple: busca por clases o IDs que contengan los datos
def extract_data():
    # Aquí debes inspeccionar el HTML real
    temperatura = soup.find('span', {'id': 'temp'}).text.strip()
    humedad = soup.find('span', {'id': 'hum'}).text.strip()
    viento = soup.find('span', {'id': 'viento'}).text.strip()
    presion = soup.find('span', {'id': 'presion'}).text.strip()
    radiacion = soup.find('span', {'id': 'radiacion'}).text.strip()
    precipitaciones = soup.find('span', {'id': 'precipitaciones'}).text.strip()

    return {
        'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'temperature': temperatura,
        'humidity': humedad,
        'wind': viento,
        'pressure': presion,
        'solar_radiation': radiacion,
        'precipitation': precipitaciones
    }

# Recoger los datos
data = extract_data()

# Guardarlo en CSV
csv_file = 'weather_data.csv'

# Comprobar si existe el CSV
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
else:
    df = pd.DataFrame([data])

df.to_csv(csv_file, index=False)
