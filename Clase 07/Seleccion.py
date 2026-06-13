class Seleccion: 
    def __init__(self, pais, confederacion):
        self.pais = pais
        self.confederacion = confederacion
        self.jugadores = []
    
    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
    
    def eliminar_jugador(self, jugador):
        for jugador_en_lista in self.jugadores:
            if jugador_en_lista == jugador:
                self.jugadores.remove(jugador_en_lista)
                break

argentina = Seleccion("argentina", "CONMEBOL")
brasil = Seleccion("Brasil", "CONMENBOL")
espanna = Seleccion("espanna", "UEFA")


argentina.agregar_jugador("Lionel Messi")
argentina.agregar_jugador("Angel Di Maria")
brasil.agregar_jugador("Neymar")
espanna.agregar_jugador("Lamine Yamal")
print(argentina.jugadores)
print(brasil.jugadores)
print(espanna.jugadores)
argentina.eliminar_jugador("Angel Di Maria")
print(argentina.jugadores)