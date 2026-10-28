class HeapABBY:
    def __init__(self):
        self.elementos = []
        self.siguienteOrden = 0

    def estaVacio(self):
        return len(self.elementos) == 0

    def cantidad(self):
        return len(self.elementos)

    def tieneMayorPrioridad(self, primero, segundo):
        if primero[0] != segundo[0]:
            return primero[0] > segundo[0]
        return primero[1] < segundo[1]

    def insertar(self, videojuego, puntuacion):
        elemento = (puntuacion, self.siguienteOrden, videojuego)
        self.siguienteOrden += 1

        self.elementos.append(elemento)
        posicion = len(self.elementos) - 1

        while posicion > 0:
            padre = (posicion - 1) // 2

            if not self.tieneMayorPrioridad(
                self.elementos[posicion],
                self.elementos[padre]
            ):
                break

            self.elementos[posicion], self.elementos[padre] = (
                self.elementos[padre],
                self.elementos[posicion]
            )

            posicion = padre

    def extraerMaximo(self):
        if self.estaVacio():
            return None

        maximo = self.elementos[0]
        ultimo = self.elementos.pop()

        if not self.estaVacio():
            self.elementos[0] = ultimo
            posicion = 0

            while True:
                izquierdo = 2 * posicion + 1
                derecho = 2 * posicion + 2
                mayor = posicion

                if (
                    izquierdo < self.cantidad()
                    and self.tieneMayorPrioridad(
                        self.elementos[izquierdo],
                        self.elementos[mayor]
                    )
                ):
                    mayor = izquierdo

                if (
                    derecho < self.cantidad()
                    and self.tieneMayorPrioridad(
                        self.elementos[derecho],
                        self.elementos[mayor]
                    )
                ):
                    mayor = derecho

                if mayor == posicion:
                    break

                self.elementos[posicion], self.elementos[mayor] = (
                    self.elementos[mayor],
                    self.elementos[posicion]
                )

                posicion = mayor

        return maximo[2]

    def construir(self, videojuegos, plataforma):
        self.elementos = []

        for orden, videojuego in enumerate(videojuegos):
            puntuacion = (
                videojuego.obtener_calificacion_por_plataforma(
                    plataforma
                )
            )

            self.elementos.append(
                (puntuacion, orden, videojuego)
            )

        self.siguienteOrden = len(self.elementos)

        for posicion in range(
            len(self.elementos) // 2 - 1, -1, -1
        ):
            self._bajar(posicion)

    def _bajar(self, posicion):
        while True:
            izquierdo = 2 * posicion + 1
            derecho = 2 * posicion + 2
            mayor = posicion

            if (
                izquierdo < self.cantidad()
                and self.tieneMayorPrioridad(
                    self.elementos[izquierdo],
                    self.elementos[mayor]
                )
            ):
                mayor = izquierdo

            if (
                derecho < self.cantidad()
                and self.tieneMayorPrioridad(
                    self.elementos[derecho],
                    self.elementos[mayor]
                )
            ):
                mayor = derecho

            if mayor == posicion:
                break

            self.elementos[posicion], self.elementos[mayor] = (
                self.elementos[mayor],
                self.elementos[posicion]
            )
            posicion = mayor

if __name__ == "__main__":
    heap = HeapABBY()

    heap.insertar("Juego A", 85)
    heap.insertar("Juego B", 95)
    heap.insertar("Juego C", 90)
    heap.insertar("Juego D", 95)

    print("Cantidad:", heap.cantidad())
    print("Mayor prioridad:", heap.elementos[0][2])
    print("Puntuación:", heap.elementos[0][0])

    assert heap.cantidad() == 4
    assert heap.elementos[0][2] == "Juego B"
    assert heap.elementos[0][0] == 95

    print("Prueba de inserción: correcta")

    print("\nOrden de extracción:")

    resultados = []

    while not heap.estaVacio():
        juego = heap.extraerMaximo()
        resultados.append(juego)
        print(juego)

    assert resultados == [
        "Juego B", "Juego D", "Juego C", "Juego A"
    ]
    assert heap.extraerMaximo() is None

    print("Prueba de extracción: correcta")

    class JuegoPrueba:
        def __init__(self, titulo, puntuacion):
            self.titulo = titulo
            self.puntuacion = puntuacion

        def obtener_calificacion_por_plataforma(self, plataforma):
            return self.puntuacion

    juegos = [
        JuegoPrueba("Juego A", 85),
        JuegoPrueba("Juego B", 95),
        JuegoPrueba("Juego C", 90),
        JuegoPrueba("Juego D", 95)
    ]

    heap.construir(juegos, "Plataforma de prueba")

    resultados = []
    while not heap.estaVacio():
        resultados.append(heap.extraerMaximo().titulo)

    print("\nConstrucción desde lista:", resultados)

    assert resultados == [
        "Juego B", "Juego D", "Juego C", "Juego A"
    ]

    print("Prueba de construcción: correcta")