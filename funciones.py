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

def obtener_top11_22(df, columna='AntidepressantUse_PeoplePer1kUsingDaily_2022'):
    """
    Obtiene los 10 países con mayor consumo de antidepresivos según una columna específica.
    
    Args:
        df (pd.DataFrame): DataFrame limpio.
        columna (str): Columna a usar para ordenar.
        
    Returns:
        pd.DataFrame: Top 10 países.
    """
    # Verificar si la columna existe
    if columna not in df.columns:
        raise ValueError(f"La columna {columna} no existe en el DataFrame.")
    
    # Ordenar el DataFrame de mayor a menor según la columna especificada
    df_top10 = df.sort_values(by=columna, ascending=False).head(10)
    return df_top10

def obtener_top10_21(df, columna='AntidepressantUse_PeoplePer1kUsingDaily_2021'):
    """
    Obtiene los 10 países con mayor consumo de antidepresivos según una columna específica.
    
    Args:
        df (pd.DataFrame): DataFrame limpio.
        columna (str): Columna a usar para ordenar.
        
    Returns:
        pd.DataFrame: Top 10 países.
    """
    # Verificar si la columna existe
    if columna not in df.columns:
        raise ValueError(f"La columna {columna} no existe en el DataFrame.")
    
    # Ordenar el DataFrame de mayor a menor según la columna especificada
    df_top10 = df.sort_values(by=columna, ascending=False).head(10)
    return df_top10

def graficar_top10(df_top10, columna='AntidepressantUse_PeoplePer1kUsingDaily_2022', titulo='Top 10 Países por Consumo de Antidepresivos (2022)'):
    """
    Grafica los 10 países con mayor consumo de antidepresivos.
    
    Args:
        df_top10 (pd.DataFrame): DataFrame con los 10 países.
        columna (str): Columna a usar para la gráfica.
        titulo (str): Título de la gráfica.
    """
    plt.figure(figsize=(12, 8))
    sns.barplot(x=columna, y='country', data=df_top10, palette='viridis')
    plt.title(titulo, fontsize=16)
    plt.xlabel('Consumo de Antidepresivos por 1k Personas (Diario)', fontsize=14)
    plt.ylabel('País', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()

    