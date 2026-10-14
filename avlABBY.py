class NodoAVL:
    def __init__(self, videojuego):
        self.videojuego = videojuego
        self.izquierdo = None
        self.derecho = None
        self.altura = 1


class AVLVideojuegos:
    def __init__(self):
        self.raiz = None

    def obtenerAltura(self, nodo):
        if nodo is None:
            return 0

        return nodo.altura

    def actualizarAltura(self, nodo):
        nodo.altura = 1 + max(
            self.obtenerAltura(nodo.izquierdo),
            self.obtenerAltura(nodo.derecho)
        )

    def obtenerBalance(self, nodo):
        if nodo is None:
            return 0

        return (
            self.obtenerAltura(nodo.izquierdo)
            - self.obtenerAltura(nodo.derecho)
        )
    def rotarDerecha(self, nodo):
        nuevaRaiz = nodo.izquierdo
        subarbol = nuevaRaiz.derecho

        nuevaRaiz.derecho = nodo
        nodo.izquierdo = subarbol

        self.actualizarAltura(nodo)
        self.actualizarAltura(nuevaRaiz)

        return nuevaRaiz

    def rotarIzquierda(self, nodo):
        nuevaRaiz = nodo.derecho
        subarbol = nuevaRaiz.izquierdo

        nuevaRaiz.izquierdo = nodo
        nodo.derecho = subarbol

        self.actualizarAltura(nodo)
        self.actualizarAltura(nuevaRaiz)

        return nuevaRaiz
    def insertar(self, videojuego):
        self.raiz, insertado = self._insertar(
            self.raiz, videojuego
        )
        return insertado

    def _insertar(self, nodo, videojuego):
        if nodo is None:
            return NodoAVL(videojuego), True

        tituloNuevo = videojuego.titulo.lower()
        tituloActual = nodo.videojuego.titulo.lower()

        if tituloNuevo == tituloActual:
            return nodo, False

        if tituloNuevo < tituloActual:
            nodo.izquierdo, insertado = self._insertar(
                nodo.izquierdo, videojuego
            )
        else:
            nodo.derecho, insertado = self._insertar(
                nodo.derecho, videojuego
            )

        if not insertado:
            return nodo, False

        self.actualizarAltura(nodo)
        balance = self.obtenerBalance(nodo)

        # Caso izquierda-izquierda o izquierda-derecha.
        if balance > 1:
            if tituloNuevo > nodo.izquierdo.videojuego.titulo.lower():
                nodo.izquierdo = self.rotarIzquierda(nodo.izquierdo)

            return self.rotarDerecha(nodo), True

        # Caso derecha-derecha o derecha-izquierda.
        if balance < -1:
            if tituloNuevo < nodo.derecho.videojuego.titulo.lower():
                nodo.derecho = self.rotarDerecha(nodo.derecho)

            return self.rotarIzquierda(nodo), True

        return nodo, True

    def buscar(self, tituloBuscado):
        nodoActual = self.raiz
        tituloBuscado = tituloBuscado.lower()

        while nodoActual is not None:
            tituloActual = nodoActual.videojuego.titulo.lower()

            if tituloBuscado == tituloActual:
                return nodoActual.videojuego

            if tituloBuscado < tituloActual:
                nodoActual = nodoActual.izquierdo
            else:
                nodoActual = nodoActual.derecho

        return None

if __name__ == "__main__":
    from types import SimpleNamespace

    casos = {
        "Izquierda-izquierda": ["C", "B", "A"],
        "Derecha-derecha": ["A", "B", "C"],
        "Izquierda-derecha": ["C", "A", "B"],
        "Derecha-izquierda": ["A", "C", "B"]
    }

    for nombre, titulos in casos.items():
        arbol = AVLVideojuegos()

        for titulo in titulos:
            arbol.insertar(SimpleNamespace(titulo=titulo))

        raiz = arbol.raiz

        assert raiz.videojuego.titulo == "B"
        assert raiz.izquierdo.videojuego.titulo == "A"
        assert raiz.derecho.videojuego.titulo == "C"
        assert raiz.altura == 2
        assert arbol.obtenerBalance(raiz) == 0

        print(f"{nombre}: correcto")

    print("Las cuatro pruebas pasaron.")