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
starbucks_frame = pd.read_csv(ruta)


# =============================================================================
# 2. EXPLORACIÓN BÁSICA DE LOS DATOS
# =============================================================================

starbucks_frame.head()    # Muestra las primeras 5 filas (útil para un vistazo rápido).
starbucks_frame.tail()    # Muestra las últimas 5 filas.
starbucks_frame.shape     # Devuelve (filas, columnas).
starbucks_frame.columns   # Devuelve el nombre de todas las columnas.
starbucks_frame.index     # Devuelve la información del índice de las filas.
type(starbucks_frame)     # Confirma el tipo de objeto (pandas.core.frame.DataFrame).


# =============================================================================
# 3. MANIPULACIÓN DE COLUMNAS
# =============================================================================

# Seleccionar columnas (Varias formas)
df_reducido = starbucks_frame[["item", "fat", "type"]] # Usando doble corchete
col_fat = starbucks_frame["fat"]                       # Seleccionar una sola (recomendado)
col_fat_punto = starbucks_frame.fat                    # Seleccionar usando punto (no recomendado si hay espacios)

# Crear o modificar una columna (Si no existe, la crea; si existe, la sobrescribe)
starbucks_frame["ranking"] = 4 

# Crear una columna condicional (Guardará valores True/False)
starbucks_frame["es_bakery"] = starbucks_frame["type"] == "bakery"

# Eliminar una columna permanentemente
del starbucks_frame["es_bakery"]


# =============================================================================
# 4. RESUMEN ESTADÍSTICO Y CONTEOS
# =============================================================================

# describe(): Genera conteo, media, min, max, desviación estándar y cuartiles.
# include='all' hace que también evalúe columnas de texto.
starbucks_frame.describe(include='all')

# mean(): Calcula el promedio (la media aritmética).
starbucks_frame["calories"].mean()             # Promedio de una columna específica
starbucks_frame.mean(numeric_only=True)        # Promedio de todas las columnas numéricas

# sum(): Suma total de los valores.
starbucks_frame[['calories','fat']].sum()      # Suma total de las columnas indicadas

# value_counts(): Cuenta cuántas veces aparece cada valor único en una columna.
# Ideal para saber distribuciones (ej. cuántos productos exactos hay de tipo "bakery", "salad", etc.)
conteo_tipos = starbucks_frame['type'].value_counts()


# =============================================================================
# 5. SELECCIÓN AVANZADA: .iloc vs .loc
# =============================================================================

# ---> .iloc (Index Location): Busca estrictamente por POSICIÓN NUMÉRICA (0, 1, 2...)
starbucks_frame.iloc[0]                  # Primera fila completa
starbucks_frame.iloc[1, 0]               # Fila 1, Columna 0 (un valor específico)
starbucks_frame.iloc[2:5, 1:3]           # Rango: Filas de 2 a 4, Columnas de 1 a 2

# ---> .loc (Location): Busca estrictamente por ETIQUETA (nombres de índices o columnas)
# Primero configuramos 'item' como índice para el ejemplo
loc_starbucks = starbucks_frame.set_index('item') 

# Buscamos desde el ítem "8-Grain Roll" hasta "Banana Nut Loaf", y mostramos la columna 'calories'
loc_starbucks.loc['8-Grain Roll':'Banana Nut Loaf', ['calories']]


# =============================================================================
# 6. FILTROS CONDICIONALES Y VALORES ÚNICOS
# =============================================================================

# unique(): Devuelve un arreglo solo con los valores únicos de una columna, sin repetirlos.
# A diferencia de value_counts(), este no los cuenta, solo te dice cuáles existen.
tipos_unicos = starbucks_frame['type'].unique()

# Filtro simple: Guardar la condición en una variable ayuda a la legibilidad
filtro_bakery = starbucks_frame['type'] == 'bakery'
df_bakery = starbucks_frame[filtro_bakery]

# Filtro múltiple (OR): Usar | para "O" (cumple una condición o la otra)
filtro_salad = starbucks_frame['type'] == 'salad'
filtro_petite = starbucks_frame['type'] == 'petite'
df_salad_o_petite = starbucks_frame[filtro_salad | filtro_petite]

# Filtro múltiple (AND): Usar & para "Y" (debe cumplir ambas condiciones)
filtro_calorias = starbucks_frame['calories'] < 300
filtro_carbo = starbucks_frame['carb'] > 20
df_sano = starbucks_frame[filtro_calorias & filtro_carbo]


# =============================================================================
# 7. ORDENAMIENTO DE DATOS
# =============================================================================

# sort_values(): Ordena el DataFrame según las columnas indicadas.
# ascending=True (Menor a mayor / A-Z), ascending=False (Mayor a menor / Z-A)
starbucks_frame.sort_values(by=["fat", "calories"], ascending=True)