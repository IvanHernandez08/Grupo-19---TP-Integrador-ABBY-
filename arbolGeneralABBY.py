class NodoGeneral:
    def __init__(self, nombre, tipo, videojuego=None):
        self.nombre = nombre
        self.tipo = tipo
        self.videojuego = videojuego
        self.hijos = []

    def agregarHijo(self, nodo):
        self.hijos.append(nodo)

    def buscarHijo(self, nombre):
        for hijo in self.hijos:
            if hijo.nombre.lower() == nombre.lower():
                return hijo

        return None


class ArbolGeneralABBY:
    def __init__(self):
        self.raiz = NodoGeneral("Catálogo ABBY", "catalogo")
    def construirDesdeCatalogo(self, videojuegos):
        self.raiz = NodoGeneral("Catálogo ABBY", "catalogo")

        for videojuego in videojuegos:
            for plataforma in videojuego.plataformas:
                nodoPlataforma = self.raiz.buscarHijo(plataforma)

                if nodoPlataforma is None:
                    nodoPlataforma = NodoGeneral(
                        plataforma, "plataforma"
                    )
                    self.raiz.agregarHijo(nodoPlataforma)

                for genero in videojuego.generos:
                    nodoGenero = nodoPlataforma.buscarHijo(genero)

                    if nodoGenero is None:
                        nodoGenero = NodoGeneral(genero, "genero")
                        nodoPlataforma.agregarHijo(nodoGenero)

                    if nodoGenero.buscarHijo(videojuego.titulo) is None:
                        nodoVideojuego = NodoGeneral(
                            videojuego.titulo,
                            "videojuego",
                            videojuego
                        )
                        nodoGenero.agregarHijo(nodoVideojuego)

    def recorrerProfundidad(self):
        resultado = []

        def visitar(nodo, ruta):
            rutaActual = ruta + [nodo.nombre]
            resultado.append((nodo, rutaActual))

            for hijo in nodo.hijos:
                visitar(hijo, rutaActual)

        visitar(self.raiz, [])
        return resultado

    def recorrerPorNiveles(self):
        from collections import deque

        resultado = []
        pendientes = deque([(self.raiz, [self.raiz.nombre])])

        while pendientes:
            nodo, ruta = pendientes.popleft()
            resultado.append((nodo, ruta))

            for hijo in nodo.hijos:
                pendientes.append(
                    (hijo, ruta + [hijo.nombre])
                )

        return resultado

    def buscar(self, nombre):
        nombreBuscado = nombre.strip().lower()

        if not nombreBuscado:
            return []

        resultados = []

        for nodo, ruta in self.recorrerProfundidad():
            if nodo.nombre.lower() == nombreBuscado:
                resultados.append((nodo, ruta))

        return resultados

if __name__ == "__main__":
    import json
    from pathlib import Path
    from types import SimpleNamespace

    ruta = Path(__file__).with_name("videojuegos.json")

    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)

    videojuegos = [
        SimpleNamespace(**dato) for dato in datos
    ]

    arbol = ArbolGeneralABBY()
    arbol.construirDesdeCatalogo(videojuegos)

    print(f"Catálogo: {len(videojuegos)} videojuegos")
    print(f"Plataformas: {len(arbol.raiz.hijos)}")

    for plataforma in arbol.raiz.hijos:
        cantidadJuegos = sum(
            len(genero.hijos) for genero in plataforma.hijos
        )

        print(
            f"{plataforma.nombre}: "
            f"{len(plataforma.hijos)} géneros, "
            f"{cantidadJuegos} apariciones de videojuegos"
        )

    profundidad = arbol.recorrerProfundidad()
    niveles = arbol.recorrerPorNiveles()

    assert len(profundidad) == len(niveles)
    assert {id(nodo) for nodo, ruta in profundidad} == {
        id(nodo) for nodo, ruta in niveles
    }

    print(f"\nTotal de nodos: {len(profundidad)}")

    print("\nPrimeros 8 nodos en profundidad:")
    for nodo, ruta in profundidad[:8]:
        print(" > ".join(ruta))

    print("\nPrimeros 8 nodos por niveles:")
    for nodo, ruta in niveles[:8]:
        print(" > ".join(ruta))

    print("\nBúsqueda de Super Mario 64:")
    resultados = arbol.buscar("Super Mario 64")
    assert resultados, "No se encontró Super Mario 64"

    for nodo, ruta in resultados:
        print(" > ".join(ruta))

    assert arbol.buscar("Categoría inexistente de prueba") == []
    print("\nPruebas de recorridos y búsqueda: correctas")