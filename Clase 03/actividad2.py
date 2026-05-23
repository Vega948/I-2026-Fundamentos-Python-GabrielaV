#Mensaje de inicio
print("Bienvenido a la aplicación de cálculo de IMC")

#Preguntas de datos personales
nombre = input("Ingrese su nombre:")
Apellidos = input("Ingrese sus apellidos:")
edad = int(input("Ingrese su edad:"))
Peso = float(input("Ingrese su peso en kg:"))
Altura = float(input("Ingrese su altura en metros:"))

#Cálculo IMC
imc = Peso / (Altura ** 2)
if imc < 18.5:
    rango = "Bajo peso"
elif imc >= 18.5 and imc < 25:
    rango = "Peso normal"
elif imc >= 25 and imc < 30:
    rango = "Sobrepeso"
elif imc >= 30 and imc < 35:
    rango = "obesidad"

#Resultados IMC
print("----RESULTADOS----")
print("Nombre:", nombre, Apellidos)
print("Edad:", edad)
print("Su IMC es:", imc)
print("rango de peso:",rango)
