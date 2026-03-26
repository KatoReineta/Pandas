import pandas as pd
import numpy as np

# =============================================================================
# 1. ACCESO, LECTURA Y EXPORTACIÓN DE ARCHIVOS
# =============================================================================

ruta = r"C:\Users\renat\Desktop\Progra\Python Codigos\Pandas\starbucks.csv"

# --- LECTURA DE DATOS ---
starbucks_frame = pd.read_csv(ruta)                   # Lee archivos CSV

# df_excel = pd.read_excel('archivo.xlsx')            # Lee archivos Excel
# df_json = pd.read_json('archivo.json')              # Lee archivos JSON
# df_sql = pd.read_sql('SELECT * FROM tabla', conn)   # Lee desde base de datos SQL
# df_html = pd.read_html('url_o_archivo.html')        # Lee tablas de una web
# df_clip = pd.read_clipboard()                       # Lee datos copiados al portapapeles

# --- COPIA Y EXPORTACIÓN ---
df_copia = starbucks_frame.copy()                     # Crea una copia independiente del DataFrame

# Exportar a Excel con parámetros útiles
# starbucks_frame.to_excel(
#     "datos.xlsx", 
#     sheet_name='Menu',      # Nombre de la hoja
#     index=False,            # Evita exportar la columna de índices numéricos
#     na_rep='Sin dato',      # Qué escribir donde haya valores nulos
#     columns=['item', 'fat'] # Exportar solo columnas específicas
# )


# =============================================================================
# 2. EXPLORACIÓN BÁSICA DE LOS DATOS
# =============================================================================

print("--- PRIMERAS 5 FILAS ---")
print(starbucks_frame.head())         

print("\n--- INFORMACIÓN GENERAL DEL DATAFRAME ---")
print(starbucks_frame.info())         

starbucks_frame.tail()         # Muestra las últimas 5 filas (silencioso)
starbucks_frame.shape          # Devuelve (filas, columnas)
starbucks_frame.columns        # Devuelve el nombre de todas las columnas
starbucks_frame.index          # Devuelve la información del índice de las filas
starbucks_frame.dtypes         # Tipos de datos de todas las columnas (ej. int64, object)
starbucks_frame['fat'].dtype   # Tipo de dato de una sola columna


# =============================================================================
# 3. MANIPULACIÓN DE COLUMNAS E ÍNDICES
# =============================================================================

# Selección y eliminación
df_reducido = starbucks_frame[["item", "fat"]] # Seleccionar múltiples columnas
# del starbucks_frame["ranking"]               # Elimina una columna permanentemente (comentado para evitar errores al repetir)

# Transformación de datos
starbucks_frame.rename(columns={'item': 'Producto'})          # Renombra columnas
starbucks_frame['fat'] = starbucks_frame['fat'].astype(float) # Convierte el tipo de dato
# df['col'] = df['col'].map({'A': 'Alto', 'B': 'Bajo'})       # Reemplaza valores usando un diccionario
# df['col'] = df['col'].apply(len)                            # Aplica una función a toda la columna

# Operación condicional vectorizada (If/Else de NumPy)
starbucks_frame['es_ligero'] = np.where(starbucks_frame['calories'] < 200, 'Sí', 'No') 

# Manejo de índices
starbucks_frame.set_index('item')                             # Establece una columna como índice
starbucks_frame.reset_index(drop=True)                        # Reinicia el índice y elimina el anterior
# starbucks_frame.reset_index(inplace=True)                   # Aplica el reinicio directamente al DataFrame


# =============================================================================
# 4. LIMPIEZA DE DATOS (VALORES NULOS Y DUPLICADOS)
# =============================================================================

starbucks_frame.isnull()                  # Máscara booleana: True donde hay nulos
starbucks_frame.notnull()                 # Inverso: True donde SÍ hay datos
starbucks_frame.dropna()                  # Elimina cualquier fila que tenga algún valor nulo
starbucks_frame.fillna(0)                 # Rellena todos los valores nulos con un 0 (u otro valor)
starbucks_frame.drop_duplicates()         # Elimina filas idénticas repetidas


# =============================================================================
# 5. RESUMEN ESTADÍSTICO Y AGRUPACIÓN
# =============================================================================

print("\n--- RESUMEN ESTADÍSTICO ---")
print(starbucks_frame.describe(include='all'))   

print("\n--- CONTEO POR TIPO DE COMIDA ---")
print(starbucks_frame['type'].value_counts())    

starbucks_frame["calories"].mean()        # Promedio
starbucks_frame['fat'].sum()              # Suma total

# Agrupación (Groupby): Ideal para sacar estadísticas por categoría
starbucks_frame.groupby('type').agg({'calories': 'mean'}) # Promedio de calorías por tipo de comida


# =============================================================================
# 6. SELECCIÓN AVANZADA
# =============================================================================

# ---> Por posición numérica (.iloc y .iat)
starbucks_frame.iloc[0:2, 1:3]     # Filas de 0 a 1, Columnas de 1 a 2
starbucks_frame.iloc[[0, 2], :]    # Filas 0 y 2 específicas, todas las columnas
starbucks_frame.iat[0, 1]          # Extrae un único valor exacto (más rápido que iloc)

# ---> Por etiqueta/nombre (.loc y .at)
# starbucks_frame.loc[0:2, ['item', 'calories']]  # Rango de filas y columnas por nombre
# starbucks_frame.at[0, 'item']                   # Extrae un único valor exacto por nombre


# =============================================================================
# 7. FILTROS CONDICIONALES Y COMPARACIONES
# =============================================================================

starbucks_frame['type'].unique()          # Arreglo con valores únicos, sin repetir

# Filtros lógicos
filtro_cal = starbucks_frame['calories'] < 300
filtro_tipo = starbucks_frame['type'] == 'bakery'
df_sano = starbucks_frame[(filtro_cal) & (filtro_tipo)]   # Uso de AND (&)

print("\n--- PRODUCTOS SANOS (Menos de 300 cal y tipo bakery) ---")
print(df_sano)

# Filtros avanzados
df_lista = starbucks_frame[starbucks_frame['type'].isin(['salad', 'petite'])] # Filtra si el valor está en la lista
starbucks_frame['calories'].eq(300)       # True si es igual a 300
starbucks_frame['calories'].ne(300)       # True si NO es igual a 300

# Comprobaciones globales a lo largo de un eje
starbucks_frame.isnull().any()            # Devuelve True si ALGÚN valor es nulo en la columna
starbucks_frame.notnull().all()           # Devuelve True solo si TODOS los valores tienen datos


# =============================================================================
# 8. UNIÓN DE DATAFRAMES (MERGE)
# =============================================================================

# pd.merge(df1, df2, on='columna_comun', how='inner')     # Une dos tablas usando una columna clave en común
# how: 'inner' (intersección), 'outer' (todo), 'left' (manda la izq), 'right' (manda la der)
# left_on / right_on: Se usa si las columnas clave se llaman distinto en cada tabla


# =============================================================================
# 9. ORDENAMIENTO DE DATOS
# =============================================================================

# Ordena por una o múltiples columnas
starbucks_frame.sort_values(by=["fat", "calories"], ascending=[True, False])

# Ordena el DataFrame según su índice de filas
starbucks_frame.sort_index(ascending=True)