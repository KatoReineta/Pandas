import pandas as pd
import numpy as np

"ACCEDER AL ARCHIVO"

ruta = r"C:\Users\renat\Desktop\Progra\Python Codigos\Pandas\starbucks.csv"
starbucks_frame = pd.read_csv(ruta)
# La r le dice a Python que lea la ruta tal cual y no se confunda con las barras invertidas \
# con la opción sep=";" puede indicar que las variables se encuentran separadas por coma en la base de datos

"VISUALIZACION DE LOS DATOS"

# El comando head() nos sirve para ver como lucen las primeras 5 filas de nuestro data frame
starbucks_frame.head() # print() para ver
# El comando tail() nos sirve para ver como lucen las ultimas 5 filas de nuestro data frame
starbucks_frame.tail() # print() para ver

"TIPO DEL OBJETO"

# Podemos preguntar el tipo del objeto starbucks_frame
type(starbucks_frame) # print() para ver

"DESCRIPCION DE UN DATAFRAME"

# Este comando nos entrega cuantas observaciones y columnas hay en el dataframe
starbucks_frame.shape # print() para ver 

starbucks_frame.index # print() para ver

# Este comando nos entrega el nombre de las columnas de nuestro dataframe
starbucks_frame.columns # print() para ver

"TRABAJO CON LOS DATOS, COLUMAS Y FILAS"

# Seleccionar solo algunas columnas del dataframe(forma 1)
df1 = pd.DataFrame(starbucks_frame, columns=["fat","item", "type"])
df1 # print() para ver
starbucks_frame[["item", "fat", "type"]] # print() para ver

# si pasamos una columna que no este contenida en el dataframe, esta aparecerá con valores nulos
df_starbucks = pd.DataFrame(starbucks_frame, columns=["item", "fat", "type", "ranking"])
df_starbucks # print() para ver

# Una columna del dataframe puede ser seleccionada utilzando los parentesis de corchetes o bien utilizando el atributo punto.
starbucks_frame["fat"] # print() para ver
# Una columna del dataframe puede ser seleccionada utilzando los parentesis de corchetes o bien utilizando el atributo punto.
starbucks_frame.fat # print() para ver

# Asignación de valores a una columna
df_starbucks["ranking"]=4
df_starbucks # print() para ver

# crear una nueva columna de valores booleanos donde la columna type sea bakery
df_starbucks["boolean_type"]=df_starbucks["type"]=="bakery"
df_starbucks # print() para ver

# para eliminar la columna recien creada podemos utilizar el comando del
del df_starbucks["boolean_type"]
df_starbucks # print() para ver

"METODO .describe()"

""" 
resumen estadístico rápido de las columnas numéricas
count: El número de elementos no nulos.
Por defecto, describe() sólo se aplica a las columnas 
numéricas del DataFrame, y te devuelve una nueva tabla 
con las siguientes métricas:

mean: La media (promedio) de la columna.

std: La desviación estándar de la columna.

min: El valor mínimo.

25%: El primer cuartil (25%) o el percentil 25.

50%: La mediana (percentil 50).

75%: El tercer cuartil (75%) o el percentil 75.

max: El valor máximo. 
"""

#Descripción de las variables numéricas 
# print() para ver
starbucks_frame.describe(include='all')

starbucks_frame["calories"].mean()

starbucks_frame.mean(numeric_only=True)

starbucks_frame[['calories','fat']].sum()

starbucks_frame['calories'].sum()

""

"Acceso a filas y columnas con comando loc y comando iloc" # print() para ver

starbucks_frame.iloc[0]
starbucks_frame.iloc[1]

#Filas 1 columna 0
starbucks_frame.iloc[1,0]
#Filas 1, 0 y 2
starbucks_frame.iloc[[1,0,2],]
#fila 2 columnas 3,0,1
starbucks_frame.iloc[2, [3, 0, 1]]
#Filas de la 2 a la 4, columnas de la 1 a la 2
starbucks_frame.iloc[2:5,1:3]
starbucks_frame.iloc[[1, 2], [3, 0, 1]]

# loc utiliza las etiquetas de los indices

loc_starbucks = starbucks_frame.iloc[0:5,]
loc_starbucks

loc_starbucks.set_index('item')

loc_starbucks = loc_starbucks.set_index('item')
loc_starbucks

loc_starbucks.loc['8-Grain Roll':'Banana Nut Loaf',['calories']]

"FILTROS" # print() para ver

starbucks_frame.head(2)
starbucks_frame['type']=='bakery'

#Es recomendable que use filtros con nombres que le ayuden a identificar que se esta haciendo
Filtro_bakery = starbucks_frame['type']=='bakery'
starbucks_frame[Filtro_bakery]

#Si me interesa saber cuantos tipos de productos hay uso la funcion unique
starbucks_frame['type'].unique()

#Puedo filtrar por tipo salad y petite
Filtro_salad = starbucks_frame['type']=='salad'
Filtro_petite = starbucks_frame['type']=='petite'
starbucks_frame[Filtro_salad|Filtro_petite]

#colocando la condición dentro del dataframe
starbucks_frame[(starbucks_frame['type']=='salad') | (starbucks_frame['type']=='petite')]

#Si nos interesa encontrar todos los item bajo 300 calorias podemos usar un filtro
Filtro_calories_less_300 = starbucks_frame['calories']<300
starbucks_frame[Filtro_calories_less_300]

#Si ademas queremos items de menos de 20 gramos de carbohidratos
Filtro_carb_less_20=starbucks_frame['carb']>20
starbucks_frame[Filtro_calories_less_300&Filtro_carb_less_20]

"ORDENAR"

#Podemos ordenar la base por orden alfabetico (en reversa) en tipo e item
starbucks_frame.sort_values(by=["fat","calories"],ascending=True)