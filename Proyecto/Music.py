import os


print("BIENVENIDO A MUSICPY - SISTEMA DE REGISTRO MUSICAL")

class Cancion:
    def __init__(self, titulo, artista, album, genero, año, playlist, favorita):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.año = año
        self.playlist = playlist
        self.favorita = favorita

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Artista: {self.artista}")
        print(f"Álbum: {self.album}")
        print(f"Género: {self.genero}")
        print(f"Año de lanzamiento: {self.año}")
        print(f"Playlist: {self.playlist}")
        print(f"¿Es favorita?: {self.favorita}")

if not os.path.exists("Proyecto"):
    os.makedirs("Proyecto")

canciones = []
favoritas = 0
ruta_archivo = os.path.join("Proyecto", "Canciones.txt")

def guardar_todo_en_archivo():
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        for cancion in canciones:
            archivo.write(f"Título: {cancion.titulo}\n")
            archivo.write(f"Artista: {cancion.artista}\n")
            archivo.write(f"Album: {cancion.album}\n")
            archivo.write(f"Género: {cancion.genero}\n")
            archivo.write(f"Año de lanzamiento: {cancion.año}\n")
            archivo.write(f"Playlist: {cancion.playlist}\n")
            archivo.write(f"¿Es favorita?: {cancion.favorita}\n")
            archivo.write("\n")  # Separador entre canciones

while True: 
    print("\n-----MENÚ PRINCIPAL-----")
    
    print("1. Registrar canción")
    print("2. Ver canciones registradas")
    print("3. Buscar canción por nombre")
    print("4. Eliminar canción")
    print("5. Salir")
    
    opcion = input("Seleccione una opcion: ")

    #Registro de canciones
    if opcion== "1":
        print("\n---AGREGAR CANCION---")
        titulo = input("Titulo: ")
        artista = input("Artista: ")
        album = input("Album: ")
        genero = input("Genero: ")
        año = input("Año de lanzamiento: ")
        playlist = input("Playlist: ")
        favorita = input("¿Es favorita? (si/no): ").lower()
        if favorita == "si":
            favoritas += 1

        nueva_cancion = Cancion(titulo, artista, album, genero, año, playlist, favorita)
        canciones.append(nueva_cancion)
        guardar_todo_en_archivo()
        print("Canción registrada exitosamente.")


    # 2. Canciones registradas
    elif opcion == "2":
        print("\n---CANCIÓN REGISTRADA---")
        if not canciones:
            print("No hay canciones registradas.")
        else:
            for i, cancion in enumerate(canciones, 1):
                print(f"\n[Canción #{i}]:")
                cancion.mostrar_informacion()
      
       
       #Busqueda de canciones 
    elif opcion== "3":
        print("\n---BUSCAR CANCION---")
        buscar = input("Ingrese el nombre de la canción que desea buscar: ").lower()
        encontrada = False
        for cancion in canciones:
            if buscar == cancion.titulo.lower():
                print("Canción encontrada: ", cancion.titulo, "de", cancion.artista, "Del album", cancion.album, "del año", cancion.año)
                encontrada = True
            
        if not encontrada:
            print("Canción no encontrada.")


        #Eliminar canciones
    elif opcion == "4":
        print("\n---ELIMINAR CANCION---")
        eliminar = input("Seleccione el título de la canción a eliminar: ").lower()
        
        encontrado = False
        for cancion in canciones:
            if cancion.titulo.lower() == eliminar:
                if cancion.favorita == "si":
                    favoritas -= 1
                canciones.remove(cancion) 
                encontrado = True
                break
        
        if encontrado:
            guardar_todo_en_archivo()
            print("Canción eliminada exitosamente del sistema y del archivo.")
        else:
            print("La canción no se encuentra registrada.")
        #Salir del bucle
    
    elif opcion == "5":
        print("Gracias por usar MusicPy")
        break
 