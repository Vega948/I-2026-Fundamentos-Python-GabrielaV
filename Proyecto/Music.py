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
        print("Título:", self.titulo)
        print("Artista:", self.artista)
        print("Álbum:", self.album)
        print("Género:", self.genero)
        print("Año de lanzamiento:", self.año)
        print("Playlist:", self.playlist)
        print("¿Es favorita?:", self.favorita)

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

    #Registro de canciones
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

        #Canciones registradas
    if opcion== "2":
        print("\n---CANCIÓN REGISTRADA---")
        print("Titulo:", str(titulo))
        print("Artista:", str(artista))
        print("Album:", str(album))
        print("Genero:", str(genero))
        print("Año:", str(año))
        print("Playlist:", str(playlist))
        print("Favorita:", str(favorita))
       
       #Busqueda de canciones 
    if opcion== "3":
        buscar = input("Ingrese el nombre de la canción que desea buscar: ")
        if buscar.lower() == titulo.lower():
            print("cancion encontrada: ", titulo, "de", artista, "Del album", album, "del año", año)

        #Eliminar canciones
    if opcion== "4":
        eliminar = input("seleccione la canción a eliminar: ")
        archivo = open("Proyecto\Canciones.txt", "r")
        canciones = archivo.readlines()
        archivo.close()
        encontrado = False

        archivo = open("Proyecto\Canciones.txt", "w")

        for linea in canciones:
            if eliminar.lower() not in linea.lower():
                archivo.write(linea)
            else:
                encontrado = True
            archivo.close()
            

        #Guardado de la cancion en el archivo de texto
        archivo = open("Proyecto\Canciones.txt", "a")
        archivo.write(f"Título: {titulo}\n")
        archivo.write(f"Artista: {artista}\n")
        archivo.write(f"Album: {album}\n")
        archivo.write(f"Género: {genero}\n")
        archivo.write(f"Año de lanzamiento: {año}\n")
        archivo.write(f"Playlist: {playlist}\n")
        archivo.write(f"¿Es favorita?: {favorita}\n")
        archivo.close()

        #Salida del programa
    if opcion== "5":
        print("Gracias por usar MusicPy")
        break
        
      


