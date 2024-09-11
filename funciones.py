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

data_antidepresivos= {
    'Grupo edad': ['40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94', '95 y más'],
    'Ambos': [44.83, 60.93, 78.66, 96.74, 107.57, 115, 129.51, 155.02, 176.03, 176.42, 159.68, 100.5],
    'Hombre': [28.8, 37.47, 45.44, 52.8, 55.7, 54.46, 64.09, 80.53, 97.28, 106.7, 107.29, 64.45],
    'Mujer': [61.17, 84.53, 111.51, 139.45, 156.42, 170.3, 185.76, 213.38, 228.84, 215.75, 182.57, 112.39]
}
def grafico_consumo_antidepresivos_por_edad(data_antidepresivos):
    """
    Grafica el consumo de antidepresivos por grupo de edad.
    
    Args:
        data (dict): Diccionario con los datos de grupos de edad y consumo para 'Ambos', 'Hombre', y 'Mujer'.
    """
    # Crear DataFrame
    df = pd.DataFrame(data_antidepresivos)

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
    
data_Hipnoticos = {
        'Grupo edad': ['40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94', '95 y más'],
    'Ambos': [10.47, 16.64, 24.95, 34.37, 43.17, 55.85, 65, 75.78, 83.69, 80.71, 79.23, 68.75],
    'Hombre': [8, 12.27, 18.02, 23.58, 29.83, 38.96, 44.15, 49.52, 59.86, 59.77, 60.1, 49.85],
    'Mujer': [13, 21.03, 31.8, 44.86, 55.74, 71.28, 82.92, 96.35, 99.67, 92.53, 87.59, 74.98]
}
  
def graficar_consumo_hipnoticos_sedantes(data_Hipnoticos):
    """
    Grafica el consumo de hipnóticos y sedantes por grupo de edad con anotaciones.
    
    Args:
        data (dict): Diccionario con los datos de grupos de edad y consumo para 'Ambos', 'Hombre', y 'Mujer'.
    """
    # Crear DataFrame a partir del diccionario
    df = pd.DataFrame(data_Hipnoticos)

    # Configurar el tamaño de la figura
    plt.figure(figsize=(12, 8))

    # Graficar las columnas de consumo de hipnóticos y sedantes para cada grupo de edad
    for column in df.columns[1:]:
        plt.plot(df['Grupo edad'], df[column], marker='o', linestyle='--', label=column)

    # Añadir títulos y etiquetas
    plt.title('Consumo de Hipnóticos y Sedantes por Grupo de Edad', fontsize=16)
    plt.xlabel('Grupo de Edad', fontsize=14)
    plt.ylabel('Dosis Diaria Definida (DDD)', fontsize=14)

    # Mostrar leyenda y cuadrícula
    plt.legend(title='Categoría', loc='upper left')
    plt.grid(True)

    # Agregar anotaciones para la columna 'Ambos'
    for i, txt in enumerate(df['Ambos']):
        plt.annotate(txt, (df['Grupo edad'][i], df['Ambos'][i]))

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()
    
data_ansiloticos = {
    'Grupo edad': ['40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94', '95 y más'],
    'Ambos': [30.3, 43.28, 55.07, 64.45, 70.5, 78.84, 88.73, 94.94, 101.13, 98.57, 89.73, 69.89],
    'Hombre': [25.59, 36.62, 42.44, 45.68, 45.37, 49.19, 52.83, 55.96, 62.67, 61.83, 55.1, 42.81],
    'Mujer': [35.11, 49.98, 67.56, 82.7, 94.16, 105.92, 119.6, 125.48, 126.92, 119.3, 104.86, 78.82]
}   


def graficar_consumo_ansioiticos(data_ansiloticos):
    """
    Grafica el consumo de ansiolíticos por grupo de edad.
    
    Args:
        data (dict): Diccionario con los datos de grupos de edad y consumo para 'Ambos', 'Hombre', y 'Mujer'.
    """
    # Crear DataFrame a partir del diccionario
    df = pd.DataFrame(data_ansiloticos)

    # Configurar el tamaño de la figura
    plt.figure(figsize=(10, 6))

    # Graficar las columnas de consumo de ansiolíticos para cada grupo de edad
    for column in df.columns[1:]:
        plt.plot(df['Grupo edad'], df[column], marker='o', label=column)

    # Añadir títulos y etiquetas
    plt.title('Consumo de Ansiolíticos por Grupo de Edad', fontsize=16)
    plt.xlabel('Grupo de Edad', fontsize=14)
    plt.ylabel('Dosis Diaria Definida (DDD)', fontsize=14)

    # Mostrar leyenda y cuadrícula
    plt.legend(title='Categoría', loc='upper left')
    plt.grid(True)

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()

data_antidepresivosrenta = {
    'Nivel de renta anual (€)': ['≥100.000', '18.000-99.999', '<18.000', 'Muy baja'],
    'Ambos': [39.6, 69.0, 111.7, 168.1],
    'Hombre': [23.3, 40.1, 60.3, 87.2],
    'Mujer': [66.3, 102.8, 153.1, 217.2]
}
def antidepresivos_renta(data_antidepresivosrenta, title='Consumo de Antidepresivos por Nivel de Renta',
                                    xlabel='Nivel de Renta Anual (€)', ylabel='Dosis Diaria Definida (DDD)'):
    # Crear DataFrame
    df = pd.DataFrame(data_antidepresivosrenta)
    
    # Crear gráfico
    plt.figure(figsize=(10, 6))
    for column in df.columns[1:]:
        plt.plot(df['Nivel de renta anual (€)'], df[column], marker='o', label=column)
    
    # Personalización del gráfico
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()
data_ansioliticosrenta = {
    'Nivel de renta anual (€)': ['≥100.000', '18.-99.999', '<18.000', 'Muy baja'],
    'Ambos': [22.2, 39.2, 71.2, 165.7],
    'Hombre': [14.6, 26.0, 48.0, 154.4],
    'Mujer': [34.6, 54.7, 89.9, 172.5]
}

def ansioliticos_renta(data_ansioliticosrenta, title='Consumo de Ansiolíticos por Nivel de Renta',
                                xlabel='Nivel de Renta Anual (€)', ylabel='Dosis Diaria Definida (DDD)'):
    # Crear DataFrame
    df = pd.DataFrame(data_ansioliticosrenta)
    
    # Crear gráfico
    plt.figure(figsize=(10, 6))
    for column in df.columns[1:]:
        plt.plot(df['Nivel de renta anual (€)'], df[column], marker='o', label=column)
    
    # Personalización del gráfico
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()
    
    
data_Hipnoticosrenta= {
    'Nivel de renta anual (€)': ['≥100.000', '18.-99.999', '<18.000', 'Muy baja'],
    'Ambos': [16.2, 26.2, 46.1, 72.0],
    'Hombre': [12.7, 19.2, 30.9, 53.3],
    'Mujer': [22.0, 34.3, 58.4, 83.3]
}    

def hipnoticos_renta(data_Hipnoticosrenta, title='Consumo de Hipnóticos y Sedantes por Nivel de Renta',
                                xlabel='Nivel de Renta Anual (€)', ylabel='Dosis Diaria Definida (DDD)'):
    # Crear DataFrame
    df = pd.DataFrame(data_Hipnoticosrenta)
    
    # Crear gráfico
    plt.figure(figsize=(10, 6))
    for column in df.columns[1:]:
        plt.plot(df['Nivel de renta anual (€)'], df[column], marker='o', label=column)
    
    # Personalización del gráfico
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()
    
data_antidepresivos_situacion= {
    'Situación laboral': ['Activos', 'Desempleados'],
    'Ambos': [50.2, 97.7],
    'Hombre': [27.4, 47.9],
    'Mujer': [76.8, 137.5]
}   

def antidepresivos_situacion(data_antidepresivos_situacion, title='Consumo de Antidepresivos por Situación Laboral',
                                      xlabel='Situación Laboral', ylabel='Dosis Diaria Definida (DDD)', 
                                      palette='coolwarm'):
    # Crear DataFrame
    df = pd.DataFrame(data_antidepresivos_situacion)
    
    # Transformar el DataFrame para que sea más fácil de graficar
    df_melted = df.melt(id_vars='Situación laboral', var_name='Género', value_name='DDD')
    
    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Situación laboral', y='DDD', hue='Género', data=df_melted, palette=palette)
    
    # Personalizar el gráfico
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(title='Género')
    plt.grid(True)
    plt.tight_layout()
    
    # Mostrar el gráfico
    plt.show()


data_ansioliticos_situacion = {
    'Situación laboral': ['Activos', 'Desempleados'],
    'Ambos': [27.2, 83.2],
    'Hombre': [18.4, 67.3],
    'Mujer': [37.5, 97.1]
}    

def ansioliticos_situacion(data_ansioliticos_situacion, title='Consumo de Ansioliticos por Situación Laboral',
                                      xlabel='Situación Laboral', ylabel='Dosis Diaria Definida (DDD)', 
                                      palette='coolwarm'):
    # Crear DataFrame
    df = pd.DataFrame(data_ansioliticos_situacion)
    
    # Transformar el DataFrame para que sea más fácil de graficar
    df_melted = df.melt(id_vars='Situación laboral', var_name='Género', value_name='DDD')
    
    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Situación laboral', y='DDD', hue='Género', data=df_melted, palette=palette)
    
    # Personalizar el gráfico
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(title='Género')
    plt.grid(True)
    plt.tight_layout()
    
    # Mostrar el gráfico
    plt.show()

data_Hipnoticos_situacion= {
    'Situación laboral': ['Activos', 'Desempleados'],
    'Ambos': [14.2, 34.2],
    'Hombre': [9.6, 23.7],
    'Mujer': [19.5, 43.3]
}    

def Hipnoticos_situacion(data_Hipnoticos_situacion, title='Consumo de Hipnóticos y Sedantes por Situación Laboral',
                                      xlabel='Situación Laboral', ylabel='Dosis Diaria Definida (DDD)', 
                                      palette='coolwarm'):
    # Crear DataFrame
    df = pd.DataFrame(data_Hipnoticos_situacion)
    
    # Transformar el DataFrame para que sea más fácil de graficar
    df_melted = df.melt(id_vars='Situación laboral', var_name='Género', value_name='DDD')
    
    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Situación laboral', y='DDD', hue='Género', data=df_melted, palette=palette)
    
    # Personalizar el gráfico
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(title='Género')
    plt.grid(True)
    plt.tight_layout()
    
    # Mostrar el gráfico
    plt.show()