import pandas as pd
import numpy as np

# =============================================================================
# 1. ACCESO Y LECTURA DE ARCHIVOS
# =============================================================================

# La "r" antes de las comillas indica una "raw string", evitando que Python 
# confunda las barras invertidas (\) con caracteres especiales.
ruta = r"C:\Users\renat\Desktop\Progra\Python Codigos\Pandas\starbucks.csv"

# read_csv(): Carga un archivo CSV en un DataFrame. 
# (Se puede usar sep=";" si el archivo está separado por punto y coma).
dataframe = pd.read_csv(ruta)


# =============================================================================
# 2. EXPLORACIÓN BÁSICA DE LOS DATOS
# =============================================================================

dataframe.head()    # Muestra las primeras 5 filas (útil para un vistazo rápido).
dataframe.tail()    # Muestra las últimas 5 filas.
dataframe.shape     # Devuelve (filas, columnas).
dataframe.columns   # Devuelve el nombre de todas las columnas.
dataframe.index     # Devuelve la información del índice de las filas.
type(dataframe)     # Confirma el tipo de objeto (pandas.core.frame.DataFrame).


# =============================================================================
# 3. MANIPULACIÓN DE COLUMNAS
# =============================================================================

# Seleccionar columnas (Varias formas)
df_reducido = dataframe[["item", "fat", "type"]] # Usando doble corchete
col_fat = dataframe["fat"]                       # Seleccionar una sola (recomendado)
col_fat_punto = dataframe.fat                    # Seleccionar usando punto (no recomendado si hay espacios)

# Crear o modificar una columna (Si no existe, la crea; si existe, la sobrescribe)
dataframe["ranking"] = 4 

# Crear una columna condicional (Guardará valores True/False)
dataframe["es_bakery"] = dataframe["type"] == "bakery"

# Eliminar una columna permanentemente
del dataframe["es_bakery"]


# =============================================================================
# 4. RESUMEN ESTADÍSTICO Y CONTEOS
# =============================================================================

# describe(): Genera conteo, media, min, max, desviación estándar y cuartiles.
# include='all' hace que también evalúe columnas de texto.
dataframe.describe(include='all')

# mean(): Calcula el promedio (la media aritmética).
dataframe["calories"].mean()             # Promedio de una columna específica
dataframe.mean(numeric_only=True)        # Promedio de todas las columnas numéricas

# sum(): Suma total de los valores.
dataframe[['calories','fat']].sum()      # Suma total de las columnas indicadas

# value_counts(): Cuenta cuántas veces aparece cada valor único en una columna.
# Ideal para saber distribuciones (ej. cuántos productos exactos hay de tipo "bakery", "salad", etc.)
conteo_tipos = dataframe['type'].value_counts()


# =============================================================================
# 5. SELECCIÓN AVANZADA: .iloc vs .loc
# =============================================================================

# ---> .iloc (Index Location): Busca estrictamente por POSICIÓN NUMÉRICA (0, 1, 2...)
dataframe.iloc[0]                  # Primera fila completa
dataframe.iloc[1, 0]               # Fila 1, Columna 0 (un valor específico)
dataframe.iloc[2:5, 1:3]           # Rango: Filas de 2 a 4, Columnas de 1 a 2

# ---> .loc (Location): Busca estrictamente por ETIQUETA (nombres de índices o columnas)
# Primero configuramos 'item' como índice para el ejemplo
loc_starbucks = dataframe.set_index('item') 

# Buscamos desde el ítem "8-Grain Roll" hasta "Banana Nut Loaf", y mostramos la columna 'calories'
loc_starbucks.loc['8-Grain Roll':'Banana Nut Loaf', ['calories']]


# =============================================================================
# 6. FILTROS CONDICIONALES Y VALORES ÚNICOS
# =============================================================================

# unique(): Devuelve un arreglo solo con los valores únicos de una columna, sin repetirlos.
# A diferencia de value_counts(), este no los cuenta, solo te dice cuáles existen.
tipos_unicos = dataframe['type'].unique()

# Filtro simple: Guardar la condición en una variable ayuda a la legibilidad
filtro_bakery = dataframe['type'] == 'bakery'
df_bakery = dataframe[filtro_bakery]

# Filtro múltiple (OR): Usar | para "O" (cumple una condición o la otra)
filtro_salad = dataframe['type'] == 'salad'
filtro_petite = dataframe['type'] == 'petite'
df_salad_o_petite = dataframe[filtro_salad | filtro_petite]

# Filtro múltiple (AND): Usar & para "Y" (debe cumplir ambas condiciones)
filtro_calorias = dataframe['calories'] < 300
filtro_carbo = dataframe['carb'] > 20
df_sano = dataframe[filtro_calorias & filtro_carbo]


# =============================================================================
# 7. ORDENAMIENTO DE DATOS
# =============================================================================

# sort_values(): Ordena el DataFrame según las columnas indicadas.
# ascending=True (Menor a mayor / A-Z), ascending=False (Mayor a menor / Z-A)
dataframe.sort_values(by=["fat", "calories"], ascending=True)