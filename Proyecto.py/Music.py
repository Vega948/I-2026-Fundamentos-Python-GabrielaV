print ("=== Sistema de regustro de música ===")
cantidad = int(input("¿Cuántas canciones desea registrar? "))

for i in range(cantidad):
    print(f"\nRegistro de canción {i+1}:")
    titulo = input("Ingrese el título de la canción: ")
    artista = input("Ingrese el nombre del artista: ")
    album = input("Ingrese el nombre del álbum: ")
    genero = input("Ingrese el género musical: ")
    duracion = input("Ingrese la duración de la canción (en minutos): ")

    print("\nInformación de la canción registrada:")
    print(f"Título: {titulo}")
    print(f"Artista: {artista}")
    print(f"Álbum: {album}")
    print(f"Género: {genero}")
    print(f"Duración: {duracion} minutos")