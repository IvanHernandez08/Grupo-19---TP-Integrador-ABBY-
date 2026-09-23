#cabecera
titulo = """
   █████████   ███████████  ███████████  █████ █████
  ███░░░░░███ ░░███░░░░░███░░███░░░░░███░░███ ░░███ 
 ░███    ░███  ░███    ░███ ░███    ░███ ░░███ ███  
 ░███████████  ░██████████  ░██████████   ░░█████   
 ░███░░░░░███  ░███░░░░░███ ░███░░░░░███   ░░███    
 ░███    ░███  ░███    ░███ ░███    ░███    ░███    
 █████   █████ ███████████  ███████████     █████   
░░░░░   ░░░░░ ░░░░░░░░░░░  ░░░░░░░░░░░     ░░░░░                                                                                                           
"""
linea = f"===================================================="

def cabecera():
    print(linea)
    print(titulo)
    print(linea)
    print(f"\n")

cabecera()

#clases y objetos (TP1)

import json


class Videojuego:
    def __init__(
        self,
        id_videojuego,
        titulo,
        desarrollador,
        generos,
        plataformas,
        calificacion,
        calificaciones
    ):
        self._id = id_videojuego
        self._titulo = titulo
        self._desarrollador = desarrollador
        self._generos = generos
        self._plataformas = plataformas
        self._calificacion = calificacion
        self._calificaciones = calificaciones

    @property
    def titulo(self):
        return self._titulo

    @property
    def desarrollador(self):
        return self._desarrollador

    @property
    def generos(self):
        return self._generos

    @property
    def plataformas(self):
        return self._plataformas

    @property
    def calificacion(self):
        return self._calificacion

    def obtener_calificacion_por_plataforma(self, plataforma):
        for nombre_plataforma, puntuacion in self._calificaciones.items():
            if nombre_plataforma.lower() == plataforma.lower():
                return puntuacion

        return self._calificacion

    def __str__(self):
        return (
            f"Título: {self._titulo}\n"
            f"Desarrollador: {self._desarrollador}\n"
            f"Géneros: {', '.join(self._generos)}\n"
            f"Plataformas: {', '.join(self._plataformas)}\n"
            f"Calificación: {self._calificacion}"
        )


with open("videojuegos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)


catalogo = []

for dato in datos:
    videojuego = Videojuego(
        dato["id"],
        dato["titulo"],
        dato["desarrollador"],
        dato["generos"],
        dato["plataformas"],
        dato["calificacion"],
        dato.get("calificaciones", {})
    )

    catalogo.append(videojuego)

class CatalogoVideojuegos:
    def __init__(self, videojuegos):
        self._videojuegos = videojuegos

    def listar(self):
        return self._videojuegos

    def buscar_por_titulo(self, titulo_buscado):
        resultados = []

        for videojuego in self._videojuegos:
            if titulo_buscado.lower() in videojuego.titulo.lower():
                resultados.append(videojuego)

        return resultados

    def filtrar_por_genero(self, genero_buscado):
        resultados = []

        for videojuego in self._videojuegos:
            for genero in videojuego.generos:
                if genero_buscado.lower() in genero.lower():
                    resultados.append(videojuego)
                    break

        return resultados

    def filtrar_por_plataforma(self, plataforma_buscada):
        resultados = []

        for videojuego in self._videojuegos:
            for plataforma in videojuego.plataformas:
                if plataforma_buscada.lower() == plataforma.lower():
                    resultados.append(videojuego)
                    break

        resultados.sort(
            key=lambda videojuego: videojuego.obtener_calificacion_por_plataforma(
                plataforma_buscada
            ),
            reverse=True
        )

        return resultados[:20]

catalogo_videojuegos = CatalogoVideojuegos(catalogo)

def ejecutar_busqueda_por_genero(catalogo):
    genero_buscado = input(
        "\n¿Qué género estás buscando?: "
    ).strip()

    if genero_buscado == "":
        print("\nNo ingresaste nada -_-")
        print("Vamos de vuelta")
        ejecutar_busqueda_por_genero(catalogo)
        return

    resultados = catalogo.filtrar_por_genero(genero_buscado)

    if len(resultados) == 0:
        print(
            f"\nNo encontramos videojuegos del género '{genero_buscado}'... o capaz lo escribiste mal ."
        )
        print("Vamos de vuelta")
        ejecutar_busqueda_por_genero(catalogo)
        return

    print(
        f"\n¡Genial!conozco {len(resultados)} videojuegos del género '{genero_buscado}':\n")

    for numero, videojuego in enumerate(resultados, start=1):
        print(f"Resultado {numero}")
        print(videojuego)
        print("-" * 40)

def ejecutar_top_por_consola(catalogo):
    print("\nEstas son las plataformas de las que te puedo recomendar:")
    print("1. PlayStation 5")
    print("2. PlayStation 4")
    print("3. Xbox Series X/S")
    print("4. PC")
    print("5. Nintendo Switch")
    print("6. Nintendo Switch 2")
    print("7. PlayStation 3")
    print("8. Xbox 360")
    print("9. PlayStation 2")
    print("10. Xbox")
    print("11. GameCube")
    print("12. Dreamcast")
    print("13. PlayStation")
    print("14. Nintendo 64")
    print("15. SNES")
    print("16. Sega Genesis")
    print("17. NES")
    print("elegí la que quieras ingresando su número")

    plataformas = {
        "1": "PlayStation 5",
        "2": "PlayStation 4",
        "3": "Xbox Series X/S",
        "4": "PC",
        "5": "Nintendo Switch",
        "6": "Nintendo Switch 2",
        "7": "PlayStation 3",
        "8": "Xbox 360",
        "9": "PlayStation 2",
        "10": "Xbox",
        "11": "GameCube",
        "12": "Dreamcast",
        "13": "PlayStation",
        "14": "Nintendo 64",
        "15": "SNES",
        "16": "Sega Genesis",
        "17": "NES"
    }

    while True:
        opcion_plataforma = input(
            "\nSeleccioná una plataforma: "
        ).strip()

        if opcion_plataforma in plataformas:
            plataforma_elegida = plataformas[opcion_plataforma]
            break

        print(
            "\n¡Opción inválida! Probá de vuelta"
        )

    resultados = catalogo.filtrar_por_plataforma(
        plataforma_elegida
    )

    if len(resultados) == 0:
        print(
            f"\nNo encontramos videojuegos para "
            f"{plataforma_elegida}."
        )
        return

    print(
        f"¡Genial! te comparto mi \nTop {len(resultados)} de {plataforma_elegida}:\n"
    )

    for posicion, videojuego in enumerate(resultados, start=1):
        puntuacion = videojuego.obtener_calificacion_por_plataforma(
            plataforma_elegida
        )

        print(f"{posicion}. {videojuego.titulo}")
        print(f"   Desarrollador: {videojuego.desarrollador}")
        print(f"   Géneros: {', '.join(videojuego.generos)}")
        print(f"   Calificación: {puntuacion}")
        print("-" * 40)

def mostrar_menu_principal():
    print("""
¡Hola! ¡Soy ABBY! tu recomendadora de juegos y te explicaré cómo trabajo: tengo 2 modos de búsqueda, en el primero
llamado "Búsqueda por género" accedes ingresando "1" donde se indica, luego tendrás que ingresar sobre qué 
género en particular estás buscando títulos (shooters, peleas, etc.) mientras que si accedes al segundo llammado
"Top por consola" ingresando "2" donde se indica, te mostraré una lista de los mejores juegos de la consola que
me digas (te aclaro que no tengo todas, cuando elijas esa opción te digo de cuáles sí te puedo decir).
Una vez dicho eso... ¿Qué tipo de búsqueda querés realizar?
            """)
    while True:
        print("acordate de que que:")
        print("\t1. Búsqueda por género")
        print("\t2. Top por consola")

        opcion = input("\nSeleccioná una opción: ").strip()

        if opcion == "1":
            print("\n¡Perfecto! Ingresaste al modo Búsqueda por género.")
            ejecutar_busqueda_por_genero(catalogo_videojuegos)
            print("\n¡Espero haberte ayudado!")
            break

        elif opcion == "2":
            print("\n¡Perfecto! Ingresaste al modo Top por consola.")
            ejecutar_top_por_consola(catalogo_videojuegos)
            print("\n¡Espero haberte ayudado!")
            break

        else:
            print(f"\n'{opcion}' no es una opción válida. Solamente podés ingresar 1 o 2.")


mostrar_menu_principal()