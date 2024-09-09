import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

archivo_excel = 'Tablas_datos_Salud_metal.xlsx'

Hoja_Farmacos = pd.read_excel('archivo_excel', sheet_name='Fármacos')
Hoja_Prevalencia = pd.read_excel('archivo_excel', sheet_name='Prevalencia variables BDCAP')