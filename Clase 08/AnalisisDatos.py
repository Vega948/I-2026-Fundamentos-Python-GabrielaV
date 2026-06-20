import pandas

# Cargar el archivo CSV
datos = pandas.read_csv("Clase 08/estudiantes.csv")

#Mostrar las primeras filas del DataFrame
print(datos.head(2))

#Mostrar solo las columnas  "Nombre" y "Apellido"
print(datos[["Nombre", "Apellido"]].head(5))

#calcualr estadisticas descriptivas
print(datos.describe(3))

#Calcular la media de la columna "edad"
print(datos["Edad"].max())

#Calcular el minimo de la columna "edad"
print(datos["Edad"].min())

#filtrar los estudiantes mayor a 85
estudiantes_alta_nota = datos[datos["Nota"] > 85]
print(estudiantes_alta_nota)

#agrupar por genero y calcular la media de la notas
media_notas_por_genero = datos.groupby("sexo")["Nota"].mean()
