import pandas as pd
import numpy as np

# =============================================================================
# 1. CREACIÓN DE UN DATAFRAME
# Un DataFrame es una estructura bidimensional (tablas con filas y columnas).
# =============================================================================

# FORMA A: Desde diccionarios de Series
cursos = pd.Series({'Algebra': 40, 'Calculo': 50, 'Introducion': 60, 'Ciencia de datos': 45})
notas = pd.Series({'Algebra': 54, 'Calculo': 33, 'Introducion': 55, 'Ciencia de datos': 60})
df_materias = pd.DataFrame({'n_estudiantes': cursos, 'prom_notas': notas})

# FORMA B: Desde un Diccionario de Listas (La forma más común)
# Las claves son las columnas, las listas son las filas.
datos_dicc = {
    'Nombre': ['Ana', 'Luis', 'Carlos'],
    'Edad': [23, 25, 30]
}
df_dicc = pd.DataFrame(datos_dicc)

# FORMA C: Desde una Lista de Diccionarios
# Cada diccionario representa una fila completa.
datos_filas = [
    {'Nombre': 'Ana', 'Edad': 23},
    {'Nombre': 'Luis', 'Edad': 25},
    {'Nombre': 'Carlos', 'Edad': 30}
]
df_filas = pd.DataFrame(datos_filas)

# FORMA D: Desde una Lista de Listas
# Se deben especificar explícitamente los nombres de las columnas.
datos_listas = [
    ['Ana', 23],
    ['Luis', 25],
    ['Carlos', 30]
]
df_listas = pd.DataFrame(datos_listas, columns=['Nombre', 'Edad'])


# =============================================================================
# 2. ATRIBUTOS PRINCIPALES
# =============================================================================

print(df_materias.index)   # Muestra las etiquetas de las filas (índice)
print(df_materias.columns) # Muestra los nombres de las columnas
print(df_materias.values)  # Devuelve los datos puros en formato de matriz NumPy
print(df_materias.size)    # Número total de elementos (filas x columnas)
print(df_materias.shape)   # Devuelve una tupla con (n_filas, n_columnas)


# =============================================================================
# 3. MANEJO DE ÍNDICES
# =============================================================================

# reset_index(): Convierte el índice actual en una columna normal y crea un nuevo índice numérico (0, 1, 2...).
df_reseteado = df_materias.reset_index()

# set_index(): Asigna una de las columnas existentes para que actúe como el nuevo índice de las filas.
df_nuevo_indice = df_reseteado.set_index('prom_notas')