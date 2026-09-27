from arbolVideojuegos import ArbolVideojuegos


class VideojuegoPrueba:
    def __init__(self, titulo):
        self.titulo = titulo

    def __str__(self):
        return self.titulo


arbol = ArbolVideojuegos()

titulos = [
    "Returnal",
    "Balatro",
    "Zelda",
    "God of War",
    "Halo 2",
    "Persona 3 Reload"
]

for titulo in titulos:
    videojuego = VideojuegoPrueba(titulo)
    arbol.insertar(videojuego)


print("BÚSQUEDA DE UN TÍTULO EXISTENTE")

resultado = arbol.buscar("Zelda")

if resultado is not None:
    print(f"Videojuego encontrado: {resultado}")
else:
    print("Videojuego no encontrado")


print("\nBÚSQUEDA DE UN TÍTULO INEXISTENTE")

resultado = arbol.buscar("Resident Evil 20")

if resultado is not None:
    print(f"Videojuego encontrado: {resultado}")
else:
    print("Videojuego no encontrado")


print("\nRECORRIDO INORDEN")

for videojuego in arbol.recorrer_inorden():
    print(videojuego)


print("\nRECORRIDO PREORDEN")

for videojuego in arbol.recorrer_preorden():
    print(videojuego)


print("\nRECORRIDO POSTORDEN")

for videojuego in arbol.recorrer_postorden():
    print(videojuego)