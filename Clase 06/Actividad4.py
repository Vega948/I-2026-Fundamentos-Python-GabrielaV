contador = 0
while True: 
    #Registro de estudiantes
    print("Bienvenidos al registro de estudiantes")
    Nombre = input("Ingrese su nombre: ")
    Carnet = input("Ingrese su carnet: ")
    Nota = float(input("Ingrese su nota final: "))

    #contador de estudiantes registrados
    contador += 1
    print("Registro de estudiantes guardado exitosamente")
    print("Total de estudiantes registrados:", contador)


    archivo = open("Clase 06\Estudiantes.txt", "a")
    archivo.write(f"Nombre:   {Nombre}\n")
    archivo.write(f"Carnet:   {Carnet}\n")
    archivo.write(f"Nota final:  {Nota}\n")
    archivo.close()

    continuar = input("¿Desea registrar otro estudiante? (si/no): ")
    if continuar.lower() == "no": 
        break
