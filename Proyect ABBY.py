def newClass(mensaje):

    print("\n====================================")
    print(f"CAMBIANDO A: {mensaje}")
    print("====================================\n")

class Inicial:
    def __init__(self, pokemon, tipo, sprite, nivel=5):
        self.pokemon = pokemon
        self.tipo = tipo
        self.sprite = sprite
        self.nivel = nivel

    def mostrar(self):
        print(f"nombre del pokemon: {self.pokemon}")
        print(f"tipo: {self.tipo}")
        print(f"nivel: {self.nivel}")
        print(f"sprite: {self.sprite}\n")

inicialFuego = Inicial(
    "Charmander",
    "Fuego",
    "CharmanderSprite.png",
    5
)

inicialAgua = Inicial(
    "Squirtle",
    "Agua",
    "SquirtleSprite.png",
    5
)

inicialPlanta = Inicial(
    "Bulbasaur",
    "Planta",
    "BulbasaurSprite.png",
    5

)

print("INFO INICIALES:\n")
inicialFuego.mostrar()
inicialAgua.mostrar()
inicialPlanta.mostrar()
newClass("ENTRENADORES")

class Entrenador:
    def __init__(self, nombre, genero, rol, region, sprite, medallas=0):
        self.nombre = nombre
        self.genero = genero
        self.rol = rol
        self.region = region
        self.medallas = medallas
        self.sprite = sprite

    def infoEntrenador(self):
        print(f"nombre: {self.nombre}")
        print(f"genero: {self.genero}")
        print(f"rol: {self.rol}")
        print(f"region: {self.region}")
        print(f"medallas: {self.medallas}")
        print(f"sprite: {self.sprite}\n")

prota = Entrenador(
    "Rojo",
    "masculino",
    "Protagonista",
    "Kanto",
    "redSprite.png",
    0
)

rival = Entrenador(
    "Azul",
    "masculino",
    "antagonista",
    "Kanto",
    "blueSprite.png",
    0
)

protaHoenn = Entrenador(
    "Ruby",
    "femenino",
    "protagonista femenina",
    "Hoenn",
    "rubySprite.png",
    0
)

print("INFO ENTRENADORES:\n")
prota.infoEntrenador()
rival.infoEntrenador()
protaHoenn.infoEntrenador()
newClass("ELECCION DE INICIAL")

class EleccionInicial:

    def __init__(self, entrenador, inicial):
        self.entrenador = entrenador
        self.inicial = inicial


    def mostrarEleccion(self):

        print(f"{self.entrenador.nombre} eligió a {self.inicial.pokemon}")
        print(f"Tipo: {self.inicial.tipo}")
        print(f"Nivel inicial: {self.inicial.nivel}")
        print(f"Sprite del pokemon: {self.inicial.sprite}\n")


eleccion1 = EleccionInicial(
    prota,
    inicialFuego
)

eleccion2 = EleccionInicial(
    rival,
    inicialAgua
)

eleccion3 = EleccionInicial(
    protaHoenn,
    inicialPlanta
)


print("ELECCIONES DE INICIALES:\n")
eleccion1.mostrarEleccion()
eleccion2.mostrarEleccion()
eleccion3.mostrarEleccion()