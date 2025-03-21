# -*- coding: utf-8 -*-
"""data_preparation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dLNFO3MtK6XGIvuLliwcTEKDFKz9NZx9
"""

# Instalar e Importar librerias para dar lectura a los datos y mostrar cada dataframe
# !pip install pandas
import pandas as pd
import json

#-------------Conexión necesaria con Google Drive para manipular las bases de datos-------------
from google.colab import drive
drive.mount('/content/drive')

#---------------- Lectura de datos y Recoleccion de ellos ----------------
# Leemos todos los datos
DFFB = pd.read_json('/content/drive/MyDrive/Proyecto/facebook_data.json', lines=False)
DFIN = pd.read_json('/content/drive/MyDrive/Proyecto/instagram_data.json', lines=False)
DFX = pd.read_json('/content/drive/MyDrive/Proyecto/twitter_data.json', lines=False)

# Mostrar cada base de datos con info y los indices
print(DFFB.info())
print(DFIN.info())
print(DFX.info())

# Mostrar las primeras 10 filas
DFFB.head(10)

DFIN.head(10)

DFX.head(10)