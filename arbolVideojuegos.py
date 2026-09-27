class NodoVideojuego:
    def __init__(self, videojuego):
        self.videojuego = videojuego
        self.izquierdo = None
        self.derecho = None


class ArbolVideojuegos:
    def __init__(self):
        self.raiz = None

    def insertar(self, videojuego):
        nuevo_nodo = NodoVideojuego(videojuego)

        if self.raiz is None:
            self.raiz = nuevo_nodo
            return True

        nodo_actual = self.raiz
        titulo_nuevo = videojuego.titulo.lower()

        while True:
            titulo_actual = nodo_actual.videojuego.titulo.lower()

            if titulo_nuevo == titulo_actual:
                return False

            if titulo_nuevo < titulo_actual:
                if nodo_actual.izquierdo is None:
                    nodo_actual.izquierdo = nuevo_nodo
                    return True

                nodo_actual = nodo_actual.izquierdo

            else:
                if nodo_actual.derecho is None:
                    nodo_actual.derecho = nuevo_nodo
                    return True

                nodo_actual = nodo_actual.derecho

    def buscar(self, titulo_buscado):
        nodo_actual = self.raiz
        titulo_buscado = titulo_buscado.lower()

        while nodo_actual is not None:
            titulo_actual = nodo_actual.videojuego.titulo.lower()

            if titulo_buscado == titulo_actual:
                return nodo_actual.videojuego

            if titulo_buscado < titulo_actual:
                nodo_actual = nodo_actual.izquierdo
            else:
                nodo_actual = nodo_actual.derecho

        return None

    def recorrer_inorden(self):
        videojuegos = []
        self._inorden(self.raiz, videojuegos)
        return videojuegos

    def _inorden(self, nodo, videojuegos):
        if nodo is not None:
            self._inorden(nodo.izquierdo, videojuegos)
            videojuegos.append(nodo.videojuego)
            self._inorden(nodo.derecho, videojuegos)

    def recorrer_preorden(self):
        videojuegos = []
        self._preorden(self.raiz, videojuegos)
        return videojuegos

    def _preorden(self, nodo, videojuegos):
        if nodo is not None:
            videojuegos.append(nodo.videojuego)
            self._preorden(nodo.izquierdo, videojuegos)
            self._preorden(nodo.derecho, videojuegos)

    def recorrer_postorden(self):
        videojuegos = []
        self._postorden(self.raiz, videojuegos)
        return videojuegos

    def _postorden(self, nodo, videojuegos):
        if nodo is not None:
            self._postorden(nodo.izquierdo, videojuegos)
            self._postorden(nodo.derecho, videojuegos)
            videojuegos.append(nodo.videojuego)