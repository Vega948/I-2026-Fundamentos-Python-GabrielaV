print("cajero automático")
print("Bienvenido al cajero automático")
saldo = 0

while True:
    print("1. consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")
    opcion = int(input ("Seleccione una opción: "))
    if opcion == 1: 
        print("Su saldo es: ", saldo)
    elif opcion == 2:
        cantidad = int (input("Ingrese la cantidad a retirar: "))
        if cantidad > saldo: 
            print("No tiene suficiente saldo")
        else: 
            saldo = saldo - cantidad 
            print(f"Ha retirado ; {cantidad}")
    elif opcion == 3: 
        cantidad = int(input("Ingrese la cantidad a depositar: "))
        saldo = saldo + cantidad
        print(f"Ha depositado: {cantidad}")
    elif opcion == 4: 
        print("Gracias por usar el cajero automático")
    else: 
        print("Opción no válida")
        