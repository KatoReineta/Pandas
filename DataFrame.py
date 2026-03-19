import pandas as pd
import numpy as np

cursos = {'Algebra':40, 'Calculo':50, 'Introducion':60, 'Ciencia de datos':45}
cursos = pd.Series(cursos)
print(cursos)

print(cursos.index)# Idices
print(cursos.values)# Valores
print(cursos.size)# Numero de elementos

notas = {'Algebra':54, 'Calculo':33, 'Introducion':55, 'Ciencia de datos':60}
notas = pd.Series(notas)

DataFrame = pd.DataFrame({'n_estudiantes': cursos, 'prom_notas': notas})
print(DataFrame)

#resetear el indice
pd.DataFrame({'n_estudiantes': cursos, 'prom_notas': notas}).reset_index()

#Convertir la columna prom_notas en indice
pd.DataFrame({'n_estudiantes': cursos, 'prom_notas': notas}).set_index('prom_notas')

# Otras formas de Crear un DataFrame ===============================================

#Diccionario de listas o diccionario de Series 
datos = {
    'Nombre': ['Ana', 'Luis', 'Carlos'],
    'Edad': [23, 25, 30]
}

df = pd.DataFrame(datos)

#Lista de diccionarios 
#Aquí, cada diccionario es una fila.
datos = [
    {'Nombre': 'Ana', 'Edad': 23},
    {'Nombre': 'Luis', 'Edad': 25},
    {'Nombre': 'Carlos', 'Edad': 30}
]

df = pd.DataFrame(datos)

#Lista de listas (con columnas especificadas)
datos = [
    ['Ana', 23],
    ['Luis', 25],
    ['Carlos', 30]
]

df = pd.DataFrame(datos, columns=['Nombre', 'Edad'])

#Diccionario de diccionarios
datos = {
    'Edad': {'Ana': 23, 'Luis': 25, 'Carlos': 30},
    'Ciudad': {'Ana': 'Bogotá', 'Luis': 'Medellín', 'Carlos': 'Cali'}
}

df = pd.DataFrame(datos)

#Desde una Series (o varias)
serie = pd.Series({'Ana': 23, 'Luis': 25, 'Carlos': 30})
df = pd.DataFrame({'Edad': serie})