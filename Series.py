import pandas as pd
import numpy as np

# CREAR E INDICE =============================================================================

lista = [1, 3, -4, 7]
serie = pd.Series(lista)
print(serie)

serieInd = pd.Series([1, 3, -4, 7], index=['d', 'c', 'b', 'a'])
print(serieInd)

# serieInd['b'] si es un elemento
# serieInd[['d', 'b']] si es más de un elemento
print(serieInd[['d', 'b']])

seriesTuple = pd.Series((10, 20, 30))
serieDict = pd.Series({'a': 10, 'b': 20, 'c': 30})
serieSola = pd.Series(5, index=['a', 'b', 'c']) # Por cada etiqueta hay un 5

array = np.array([1, 2, 3]) # De numpy
array = pd.Series(array)
print(array)

# FILTROS =============================================================================

print(serieInd)
print('valores que cumplen la condicion serieInd < 3 ')
print(serieInd < 3)
print('valores que cumplieron la condicion serieInd < 3 ')
print(serieInd[serieInd < 3])