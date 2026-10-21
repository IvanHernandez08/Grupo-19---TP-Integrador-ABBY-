
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

import json
from arbolVideojuegos import ArbolVideojuegos
from arbolGeneralABBY import ArbolGeneralABBY

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

arbolVideojuegos = ArbolVideojuegos()

for videojuego in catalogo:
    arbolVideojuegos.insertar(videojuego)

arbolGeneral = ArbolGeneralABBY()
arbolGeneral.construirDesdeCatalogo(catalogo)


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

def ejecutar_busqueda_por_titulo(arbol):
    while True:
        titulo_buscado = input(
            "\n¿Qué videojuego estás buscando?: "
        ).strip()

        if titulo_buscado == "":
            print("\nNo ingresaste ningún título. Probá de nuevo.")
            continue

        videojuego_encontrado = arbol.buscar(titulo_buscado)

        if videojuego_encontrado is None:
            print(
                f"\nNo encontramos un videojuego llamado "
                f"'{titulo_buscado}'... o capaz lo escribiste mal"
            )
            print(
                "Revisá que el título esté escrito completo y "
                "probá nuevamente."
            )
            continue

        print("\n¡Encontré el videojuego!\n")
        print(videojuego_encontrado)
        print("-" * 40)
        break

def explorarCategorias(arbol):
    camino = [arbol.raiz]

    while True:
        nodoActual = camino[-1]

        print("\n" + " > ".join(
            nodo.nombre for nodo in camino
        ))

        if nodoActual.tipo == "videojuego":
            print()
            print(nodoActual.videojuego)

            plataforma = camino[1].nombre
            puntuacion = (
                nodoActual.videojuego
                .obtener_calificacion_por_plataforma(plataforma)
            )

            print(f"Calificación en {plataforma}: {puntuacion}")
            input("\nPresioná Enter para volver al género...")
            camino.pop()
            continue

        opciones = sorted(
            nodoActual.hijos,
            key=lambda nodo: nodo.nombre.lower()
        )

        for numero, hijo in enumerate(opciones, start=1):
            print(f"{numero}. {hijo.nombre}")

        if len(camino) > 1:
            print("0. Volver al nivel anterior")
        else:
            print("0. Terminar exploración")

        opcion = input("\nSeleccioná una opción: ").strip()

        if opcion == "0":
            if len(camino) == 1:
                return

            camino.pop()
            continue

        try:
            indice = int(opcion) - 1
        except ValueError:
            print("\n¡Opción inválida! Probá de vuelta!")
            continue

        if 0 <= indice < len(opciones):
            camino.append(opciones[indice])
        else:
            print("\n¡Opción inválida! Probá de vuelta")


def mostrar_menu_principal():
    print("""
¡Hola! ¡Soy ABBY! Tu recomendadora de videojuegos y te explicaré cómo trabajp: tengo 4 modos de búsqueda, donde 
podés buscar por género, consultar el top por consola, buscar un título completo o explorar el catálogo por categorías.
En este último, elegís una plataforma, después un género y finalmente el videojuego que querés conocer.
Una vez dicho eso... 
""")

    while True:
        print("\n¿Qué querés hacer?")
        print("\t1. Búsqueda por género")
        print("\t2. Top por consola")
        print("\t3. Búsqueda por título")
        print("\t4. Explorar categorías")
        print("\t0. Salir")

        opcion = input("\nSeleccioná una opción: ").strip()

        if opcion == "1":
            print("\n¡Perfecto! Ingresaste al modo Búsqueda por género.")
            ejecutar_busqueda_por_genero(catalogo_videojuegos)

        elif opcion == "2":
            print("\n¡Perfecto! Ingresaste al modo Top por consola.")
            ejecutar_top_por_consola(catalogo_videojuegos)

        elif opcion == "3":
            print("\n¡Perfecto! Ingresaste al modo Búsqueda por título.")
            ejecutar_busqueda_por_titulo(arbolVideojuegos)

        elif opcion == "4":
            print("\n¡Perfecto! Ingresaste al modo Explorar categorías.")
            explorarCategorias(arbolGeneral)

        elif opcion == "0":
            print("\n¡Hasta la próxima!")
            break

        else:
            print("\nOpción inválida. Ingresá 0, 1, 2, 3 o 4.")


mostrar_menu_principal()