#inicializar variables
nombre = "Gabriela"
edad= "18"


#solicitar al usuario su edad
edad:int =  int (input ("¿cual es tu edad?"))

# calcular año de nacimiento
anno_de_nacimiento:int = 2026 - edad
print (anno_de_nacimiento)
print(anno_de_nacimiento)

mayor_de_edad:bool = edad >= 18

#imprimir nombre,edad y año de nacimiento
print("mi nombre es" :{nombre})
print ("mi edad es" : {edad} )
print ("mi anno_de_nacimiento es":, {anno_de_nacimiento})

#inicializar variables
soy_yo = nombre == "Gabriela" and edad == 18
no_soy_yo = not(nombre == "Gabriela" and edad == 18)
soy_yo = (nombre == "Gabriela" and edad == 18)
quizas_soy_yo = (nombre == "Gabriela" and edad == 18)

#imprimir variable
print (soy_yo)
print (no_soy_yo)
print (quizas_soy_yo)
soy_yo = (nombre == "Gabriela" and edad == 18)
