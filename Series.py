import pandas as pd
import numpy as np

# =============================================================================
# 1. CREACIÓN DE SERIES
# Una Serie es una estructura unidimensional (como una columna de Excel).
# =============================================================================

# Desde una lista
lista = [1, 3, -4, 7]
serie_lista = pd.Series(lista)

# Desde una lista especificando un índice personalizado
serie_ind = pd.Series([1, 3, -4, 7], index=['d', 'c', 'b', 'a'])

# Desde una tupla
serie_tupla = pd.Series((10, 20, 30))

# Desde un diccionario (las claves serán el índice)
serie_dict = pd.Series({'a': 10, 'b': 20, 'c': 30})

# Desde un valor escalar (repite el número 5 para cada etiqueta del índice)
serie_sola = pd.Series(5, index=['a', 'b', 'c']) 

# Desde un arreglo de NumPy
array_np = np.array([1, 2, 3])
serie_array = pd.Series(array_np)


# =============================================================================
# 2. ATRIBUTOS PRINCIPALES DE UNA SERIE
# =============================================================================

print(serie_ind.index)  # Devuelve las etiquetas del índice
print(serie_ind.values) # Devuelve solo los valores (como un arreglo de NumPy)
print(serie_ind.size)   # Devuelve el número total de elementos


# =============================================================================
# 3. ACCESO A DATOS (INDEXING)
# =============================================================================

# Acceder a un solo elemento mediante su etiqueta
# print(serie_ind['b']) 

# Acceder a múltiples elementos (se pasa una lista de etiquetas)
# print(serie_ind[['d', 'b']])


# =============================================================================
# 4. FILTROS CONDICIONALES (MÁSCARAS BOOLEANAS)
# =============================================================================

# Devuelve una Serie de True/False indicando si se cumple la condición
condicion = serie_ind < 3
print(condicion)

# Aplica la condición a la Serie original para obtener solo los datos filtrados
datos_filtrados = serie_ind[serie_ind < 3]
print(datos_filtrados)