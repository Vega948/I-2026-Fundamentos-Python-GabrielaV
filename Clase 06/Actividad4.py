print("Bienvenidos al registro de estudiantes")
While True
Nombre = input("Ingrese su nombre: ")
Carnet = input("Ingrese su carnet: ")
Nota = float(input("Ingrese su nota final: "))

archivo = open("Clase 06\Estudiantes.txt", "a")
archivo.write(f"Nombre:   {Nombre}\n")
archivo.write(f"Carnet:   {Carnet}\n")
archivo.write(f"Nota final:  {Nota}\n")
archivo.close()
