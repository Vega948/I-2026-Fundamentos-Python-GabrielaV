print("BIENVENIDO A MUSICPY - SISTEMA DE REGISTRO MUSICAL")

canciones = []
favoritas = 0

while True: 
    print("\n-----MENÚ PRINCIPAL-----")
    
    print("1. Registrar canción")
    print("2. Ver canciones registradas")
    print("3. Buscar canción por nombre")
    print("4. Eliminar canción")
    print("5. Salir")
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion== "1":
        print("\n---AGREGAR CANCION---")
        titulo= input("Titulo: ")
        artista=input("Artista: ")
        album=input("Album: ")
        genero=input("Genero: ")
        año=input("Año de lanzamiento: ")
        playlist= input("Playlist: ")
        favorita=input("¿Es favorita? (si\no): ").lower()
        if favorita == "si":
            favoritas += 1
    if opcion== "2":
        print("\n---CANCIÓN REGISTRADA---")
        print("Titulo:", titulo)
        print("Artista:", artista)
        print("Album:", album)
        print("Genero:", genero)
        print("Año:", año)
        print("Playlist:", playlist)
        print("Favorita:", favorita)
    if opcion== "3":
        buscar = input("Ingrese el nombre de la canción que desea buscar: ")
        if buscar.lower() == titulo.lower():
            print("cancion encontrada: ", titulo, "de", artista, "Del album", album, "del año", año)
    if opcion== "4":
        


        archivo = open("Proyecto\Canciones.txt", "a")
        archivo.write(f"Título: {titulo}\n")
        archivo.write(f"Artista: {artista}\n")
        archivo.write(f"Album: {album}\n")
        archivo.write(f"Género: {genero}\n")
        archivo.write(f"Año de lanzamiento: {año}\n")
        archivo.write(f"Playlist: {playlist}\n")
        archivo.write(f"¿Es favorita?: {favorita}\n")
        archivo.close()

        continuar = input("¿Desea registrar otra canción? (si/no): ")
        if continuar.lower() == "no":
            break


