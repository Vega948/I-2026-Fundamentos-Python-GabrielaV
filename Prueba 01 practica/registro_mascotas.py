print("BIENVENIDO AL SISTEMA DE REGISTRO DE MASCOTAS")
class Mascota: 
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Especie:", self.especie)
        print("Edad:", self.edad)
        print()
mascotas = []

cantidad = int(input("Ingrese la cantidad de mascotas a registrar: "))

for i in range(cantidad):
    print(f"\n---REGISTRO DE MASCOTA---")
    nombre = input("Nombre: ")
    especie = input("Especie: ")
    edad = int(input("Edad: "))

    mascota = Mascota(nombre, especie, edad)
    mascotas.append(mascota)

    print("\n---MASCOTA REGISTRADA---")
    print("Nombre:", mascota.nombre)
    print("Especie:", mascota.especie)
    print("Edad:", mascota.edad)

for i in range(len(mascotas)):
    print(f"\n---INFORMACIÓN DE LA MASCOTA {i+1}---")
    mascotas[i].mostrar_informacion()
