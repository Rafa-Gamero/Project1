import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

archivo = 'antidepressant-use-by-country-2024.csv'

def cargar_datos(archivo):
    
    df = pd.read_csv(archivo)
    return df


def limpiar_datos(df):
    
    df = df.drop_duplicates(subset=['country'])
    
    df.replace('',pd.NA, inplace=True)
    
    columnas_numericas = df.columns.drop('country')
    for col in columnas_numericas:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Manejar valores faltantes, por ejemplo, rellenando con la mediana
    df.fillna('Sin datos', inplace=True)
    
    return df



    