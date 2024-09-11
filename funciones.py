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

def graficar_top10_por_renta(df_top10, columna_consumo='AntidepressantUse_PeoplePer1kUsingDaily_2022', columna_renta='AntidepressantUseAnnualSalesPerCapita2021', titulo='Top 10 paises consumo de antidepresivos por Renta'):
    """
     Grafica los 10 países con mayor consumo de antidepresivos según su renta.
    
    Args:
        df_top10 (pd.DataFrame): DataFrame con los 10 países.
        columna_consumo (str): Columna de consumo de antidepresivos.
        columna_renta (str): Columna de renta.
        titulo (str): Título de la gráfica.
    """
    plt.figure(figsize=(14, 10))
     # Crear gráfico de barras para el consumo
    sns.barplot(x=columna_consumo, y='country', data=df_top10, palette='Blues_d', label='Consumo (1k personas/día)')
    
    # Crear otro eje para graficar la renta
    ax2 = plt.twinx()
    sns.barplot(x=columna_renta, y='country', data=df_top10, palette='Greens_d', label='Renta per cápita (2021)', ax=ax2)
    
    # Título y etiquetas
    plt.title('Top 10 Países por Consumo de Antidepresivos y Renta (2022)', fontsize=16)
    plt.xlabel('Consumo de Antidepresivos por 1k Personas (Diario) y Renta per Cápita', fontsize=14)
    plt.ylabel('País', fontsize=14)
    
    # Ajustar el layout
    plt.tight_layout()
    
    # Mostrar gráfico
    plt.show()
    
    
    
def graficar_top10_22(top_10_22, columna='AntidepressantUse_PeoplePer1kUsingDaily_2022', titulo='Top 10 Países por Consumo de Antidepresivos (2022)'):
    """
    Grafica los 10 países con mayor consumo de antidepresivos.
    
    Args:
        df_top10_22 (pd.DataFrame): DataFrame con los 10 países.
        columna (str): Columna a usar para la gráfica.
        titulo (str): Título de la gráfica.
    """
    plt.figure(figsize=(12, 8))
    sns.barplot(x=columna, y='country', data=top_10_22, palette='viridis')
    plt.title(titulo, fontsize=16)
    plt.xlabel('Consumo de Antidepresivos por 1k Personas (Diario)', fontsize=14)
    plt.ylabel('País', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()


def graficar_top10_21(df_top_21, columna='AntidepressantUse_PeoplePer1kUsingDaily_2021', titulo='Top 10 Países por Consumo de Antidepresivos (2021)'):
    """
    Grafica los 10 países con mayor consumo de antidepresivos.
    
    Args:
        df_top10_22 (pd.DataFrame): DataFrame con los 10 países.
        columna (str): Columna a usar para la gráfica.
        titulo (str): Título de la gráfica.
    """
    plt.figure(figsize=(12, 8))
    sns.barplot(x=columna, y='country', data=df_top_21, palette='viridis')
    plt.title(titulo, fontsize=16)
    plt.xlabel('Consumo de Antidepresivos por 1k Personas (Diario)', fontsize=14)
    plt.ylabel('País', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()

data = {
    'Grupo edad': ['40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94', '95 y más'],
    'Ambos': [44.83, 60.93, 78.66, 96.74, 107.57, 115, 129.51, 155.02, 176.03, 176.42, 159.68, 100.5],
    'Hombre': [28.8, 37.47, 45.44, 52.8, 55.7, 54.46, 64.09, 80.53, 97.28, 106.7, 107.29, 64.45],
    'Mujer': [61.17, 84.53, 111.51, 139.45, 156.42, 170.3, 185.76, 213.38, 228.84, 215.75, 182.57, 112.39]
}
def graficar_consumo_antidepresivos_por_edad(data):
    """
    Grafica el consumo de antidepresivos por grupo de edad.
    
    Args:
        data (dict): Diccionario con los datos de grupos de edad y consumo para 'Ambos', 'Hombre', y 'Mujer'.
    """
    # Crear DataFrame
    df = pd.DataFrame(data)

    # Configurar la figura
    plt.figure(figsize=(10, 6))

    # Graficar cada columna
    for column in df.columns[1:]:
        plt.plot(df['Grupo edad'], df[column], marker='o', label=column)

    # Añadir título y etiquetas
    plt.title('Consumo de Antidepresivos por Grupo de Edad', fontsize=16)
    plt.xlabel('Grupo de Edad', fontsize=14)
    plt.ylabel('Dosis Diaria Definida (DDD)', fontsize=14)

    # Mostrar leyenda y cuadrícula
    plt.legend(title='Categoría', loc='upper left')
    plt.grid(True)

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()