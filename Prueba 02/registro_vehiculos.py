class Vehiculos:
    def __init__(self, Placa, marca, año):
        self.Placa = Placa
        self.marca = marca
        self.año = año

    def mostrar_informacion(self):
        print(f"Placa: {self.Placa}")
        print(f"Marca: {self.marca}")
        print(f"Año: {self.año}")

Vehiculos = []

print("\n-----Bienvenido al registro de vehículos -----")
Cantidad = int(input("Ingrese la cantidad de vehículos a registar: "))


for i in range(Cantidad):
    print(f"\n---REGISTRO DEL VEHÍCULO {i+1}---")
    Placa = int(input("Ingrese la placa del vehículo: "))
    Marca = input("Ingrese la marca del vehículo: ")
    Año = int(input("Ingrese el año del vehículo: "))

    print("---VEHÍCULO REGISTRADO---")
    print(f"Placa: {Placa}")
    print(f"Marca: {Marca}")
    print(f"Año: {Año}")
    

