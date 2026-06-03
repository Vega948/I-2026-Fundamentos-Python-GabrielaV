print("Bienvindo al Supermercado")
total_general = 0

while True:
    print("Ingrese la información de los productos que desea comprar")

    producto = input("Nombre del producto: ")
    precio = int(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad de productos: "))

    if cantidad < 1 or precio < 1:
        print("La informacion que registro es invalida")
    else:
        total = precio * cantidad
        total_general += total

        print("Producto:", producto)
        print("Precio:", precio)
        print("Cantidad:", cantidad)
        print("Total a pagar", total)

    opcion = int(input("Ingrese 1 para registrar otro producto o 2 para finalizar la compra: "))

    if opcion == 2:
        break

print("===== TOTAL A PAGAR ====")
print("Total a pagar:", total_general)