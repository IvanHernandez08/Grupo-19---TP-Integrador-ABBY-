class GrafoABBY:
    def __init__(self):
        self.videojuegos = {}
        self.adyacencia = {}

    def normalizar(self, texto):
        return texto.strip().casefold()

    def agregarVertice(self, videojuego):
        clave = self.normalizar(videojuego.titulo)

        if clave in self.videojuegos:
            return False

        self.videojuegos[clave] = videojuego
        self.adyacencia[clave] = set()
        return True

    def agregarArista(self, tituloA, tituloB):
        claveA = self.normalizar(tituloA)
        claveB = self.normalizar(tituloB)

        if claveA not in self.videojuegos:
            return False

        if claveB not in self.videojuegos:
            return False

        if claveA == claveB:
            return False

        if claveB in self.adyacencia[claveA]:
            return False

        self.adyacencia[claveA].add(claveB)
        self.adyacencia[claveB].add(claveA)
        return True

    def cantidadVertices(self):
        return len(self.videojuegos)

    def cantidadAristas(self):
        return sum(
            len(vecinos)
            for vecinos in self.adyacencia.values()
        ) // 2

    def normalizarConjunto(self, valores):
        if isinstance(valores, str):
            valores = [valores]

        return {
            self.normalizar(valor)
            for valor in valores
            if valor.strip()
        }

    def construirDesdeCatalogo(self, videojuegos):
        self.videojuegos = {}
        self.adyacencia = {}

        for videojuego in videojuegos:
            self.agregarVertice(videojuego)

        juegos = list(self.videojuegos.values())

        generos = [
            self.normalizarConjunto(juego.generos)
            for juego in juegos
        ]

        desarrolladores = [
            self.normalizarConjunto(juego.desarrollador)
            for juego in juegos
        ]

        for i in range(len(juegos)):
            for j in range(i + 1, len(juegos)):
                compartenGenero = bool(generos[i] & generos[j])
                compartenDesarrollador = bool(
                    desarrolladores[i] & desarrolladores[j]
                )

                if compartenGenero and compartenDesarrollador:
                    self.agregarArista(
                        juegos[i].titulo,
                        juegos[j].titulo
                    )

    def calcularDensidad(self):
        vertices = self.cantidadVertices()

        if vertices < 2:
            return 0.0

        posibles = vertices * (vertices - 1) // 2
        return self.cantidadAristas() / posibles

    def obtenerRelacionados(self, titulo):
        clave = self.normalizar(titulo)

        if clave not in self.videojuegos:
            return None

        relacionados = [
            self.videojuegos[vecino]
            for vecino in self.adyacencia[clave]
        ]

        return sorted(
            relacionados,
            key=lambda juego: self.normalizar(juego.titulo)
        )

    def obtenerMotivoRelacion(self, tituloA, tituloB):
        claveA = self.normalizar(tituloA)
        claveB = self.normalizar(tituloB)

        if claveA not in self.videojuegos:
            return None

        if claveB not in self.adyacencia[claveA]:
            return None

        juegoA = self.videojuegos[claveA]
        juegoB = self.videojuegos[claveB]

        generosCompartidos = (
            self.normalizarConjunto(juegoA.generos)
            & self.normalizarConjunto(juegoB.generos)
        )

        desarrolladoresCompartidos = (
            self.normalizarConjunto(juegoA.desarrollador)
            & self.normalizarConjunto(juegoB.desarrollador)
        )

        return {
            "generos": sorted(generosCompartidos),
            "desarrolladores": sorted(desarrolladoresCompartidos)
        }

    def buscarCamino(self, tituloOrigen, tituloDestino):
        from collections import deque

        origen = self.normalizar(tituloOrigen)
        destino = self.normalizar(tituloDestino)

        if origen not in self.videojuegos:
            return None

        if destino not in self.videojuegos:
            return None

        pendientes = deque([origen])
        anteriores = {origen: None}

        while pendientes:
            actual = pendientes.popleft()

            if actual == destino:
                camino = []

                while actual is not None:
                    camino.append(self.videojuegos[actual])
                    actual = anteriores[actual]

                camino.reverse()
                return camino

            for vecino in sorted(self.adyacencia[actual]):
                if vecino not in anteriores:
                    anteriores[vecino] = actual
                    pendientes.append(vecino)

        return []

    def buscarRelacionadoPorPlataforma(self, tituloOrigen, plataforma):
        from collections import deque

        origen = self.normalizar(tituloOrigen)
        plataformaBuscada = self.normalizar(plataforma)

        if origen not in self.videojuegos:
            return None

        pendientes = deque([origen])
        anteriores = {origen: None}

        while pendientes:
            actual = pendientes.popleft()
            juego = self.videojuegos[actual]

            if actual != origen and any(
                self.normalizar(nombre) == plataformaBuscada
                for nombre in juego.plataformas
            ):
                camino = []
                while actual is not None:
                    camino.append(self.videojuegos[actual])
                    actual = anteriores[actual]

                camino.reverse()
                return camino

            for vecino in sorted(self.adyacencia[actual]):
                if vecino not in anteriores:
                    anteriores[vecino] = actual
                    pendientes.append(vecino)

        return []

    def explorarConexionesDFS(self, tituloOrigen):
        origen = self.normalizar(tituloOrigen)

        if origen not in self.videojuegos:
            return None

        visitados = {origen}
        relacionados = []

        def visitar(actual):
            for vecino in sorted(self.adyacencia[actual]):
                if vecino in visitados:
                    continue

                visitados.add(vecino)
                relacionados.append(self.videojuegos[vecino])
                visitar(vecino)

        visitar(origen)
        return relacionados

if __name__ == "__main__":
    from types import SimpleNamespace

    grafo = GrafoABBY()

    juegoA = SimpleNamespace(titulo="Juego A")
    juegoB = SimpleNamespace(titulo="Juego B")

    assert grafo.agregarVertice(juegoA)
    assert grafo.agregarVertice(juegoB)
    assert not grafo.agregarVertice(juegoA)

    assert grafo.agregarArista("Juego A", "Juego B")
    assert not grafo.agregarArista("Juego B", "Juego A")
    assert not grafo.agregarArista("Juego A", "Juego A")
    assert not grafo.agregarArista("Juego A", "Inexistente")

    assert "juego b" in grafo.adyacencia["juego a"]
    assert "juego a" in grafo.adyacencia["juego b"]

    print("Vértices:", grafo.cantidadVertices())
    print("Aristas:", grafo.cantidadAristas())
    print("Pruebas iniciales del grafo: correctas")


    import json
    from pathlib import Path

    ruta = Path(__file__).with_name("videojuegos.json")

    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)

    catalogo = [
        SimpleNamespace(**dato) for dato in datos
    ]

    grafo.construirDesdeCatalogo(catalogo)

    for clave, vecinos in grafo.adyacencia.items():
        assert clave not in vecinos

        for vecino in vecinos:
            assert clave in grafo.adyacencia[vecino]

    print("\nGrafo del catálogo:")
    print("Vértices:", grafo.cantidadVertices())
    print("Aristas:", grafo.cantidadAristas())
    print(f"Densidad: {grafo.calcularDensidad():.2%}")
    print("Construcción y simetría: correctas")

    print("\nRelacionados con Elden Ring:")

    relacionados = grafo.obtenerRelacionados("Elden Ring")
    assert relacionados is not None

    assert {juego.titulo for juego in relacionados} == {
        "Bloodborne",
        "Elden Ring: Shadow of the Erdtree"
    }

    for juego in relacionados:
        motivo = grafo.obtenerMotivoRelacion(
            "Elden Ring", juego.titulo
        )

        assert motivo["generos"]
        assert motivo["desarrolladores"]

        print(f"\n- {juego.titulo}")
        print("  Géneros:", ", ".join(motivo["generos"]))
        print(
            "  Desarrolladores:",
            ", ".join(motivo["desarrolladores"])
        )

    assert grafo.obtenerRelacionados("ELDEN RING") == relacionados
    assert grafo.obtenerRelacionados("Título inexistente de prueba") is None

    aislados = [
        clave
        for clave, vecinos in grafo.adyacencia.items()
        if not vecinos
    ]

    if aislados:
        tituloAislado = grafo.videojuegos[aislados[0]].titulo
        assert grafo.obtenerRelacionados(tituloAislado) == []
        print(f"\nEjemplo sin conexiones: {tituloAislado}")

    print("\nPruebas de relacionados: correctas")

    print("\nCamino entre Elden Ring y Bloodborne:")

    camino = grafo.buscarCamino("Elden Ring", "Bloodborne")

    assert camino is not None
    assert [juego.titulo for juego in camino] == [
        "Elden Ring", "Bloodborne"
    ]

    print(" > ".join(juego.titulo for juego in camino))

    mismoJuego = grafo.buscarCamino("Elden Ring", "ELDEN RING")
    assert [juego.titulo for juego in mismoJuego] == ["Elden Ring"]

    assert grafo.buscarCamino("Elden Ring", "Astro Bot") == []
    assert grafo.buscarCamino(
        "Elden Ring", "Título inexistente de prueba"
    ) is None

    grafoPrueba = GrafoABBY()

    for titulo in ("A", "B", "C", "D"):
        grafoPrueba.agregarVertice(
            SimpleNamespace(titulo=titulo)
        )

    grafoPrueba.agregarArista("A", "B")
    grafoPrueba.agregarArista("B", "C")
    grafoPrueba.agregarArista("C", "A")
    grafoPrueba.agregarArista("C", "D")

    caminoPrueba = grafoPrueba.buscarCamino("A", "D")

    assert [juego.titulo for juego in caminoPrueba] == [
        "A", "C", "D"
    ]

    print(
        "Camino de prueba:",
        " > ".join(juego.titulo for juego in caminoPrueba)
    )
    print("Pruebas de caminos: correctas")

    grafoPlataformas = GrafoABBY()

    for titulo, plataformas in (
        ("Inicio", ["PC"]),
        ("Puente", ["Xbox 360"]),
        ("Candidato", ["PlayStation 4"]),
        ("Aislado", ["PlayStation 4"]),
    ):
        grafoPlataformas.agregarVertice(
            SimpleNamespace(titulo=titulo, plataformas=plataformas)
        )

    grafoPlataformas.agregarArista("Inicio", "Puente")
    grafoPlataformas.agregarArista("Puente", "Candidato")

    camino = grafoPlataformas.buscarRelacionadoPorPlataforma(
        "Inicio", "playstation 4"
    )

    assert [juego.titulo for juego in camino] == [
        "Inicio", "Puente", "Candidato"
    ]
    assert grafoPlataformas.buscarRelacionadoPorPlataforma(
        "Inicio", "PC"
    ) == []
    assert grafoPlataformas.buscarRelacionadoPorPlataforma(
        "Inexistente", "PC"
    ) is None

    print("\nBFS por plataforma:", " > ".join(
        juego.titulo for juego in camino
    ))
    print("Pruebas de BFS por plataforma: correctas")

    explorados = grafoPrueba.explorarConexionesDFS("a")
    titulos = [juego.titulo for juego in explorados]

    assert titulos == ["B", "C", "D"]
    assert grafoPlataformas.explorarConexionesDFS("Aislado") == []
    assert grafoPrueba.explorarConexionesDFS("Inexistente") is None

    print("\nDFS desde A:", ", ".join(titulos))
    print("Pruebas de DFS: correctas")