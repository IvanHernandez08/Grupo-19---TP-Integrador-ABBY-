import json
from pathlib import Path
from types import SimpleNamespace
from timeit import repeat

from arbolVideojuegos import ArbolVideojuegos
from avlABBY import AVLVideojuegos


def calcularAltura(raiz):
    if raiz is None:
        return 0

    pendientes = [(raiz, 1)]
    altura = 0

    while pendientes:
        nodo, nivel = pendientes.pop()
        altura = max(altura, nivel)

        if nodo.izquierdo is not None:
            pendientes.append((nodo.izquierdo, nivel + 1))

        if nodo.derecho is not None:
            pendientes.append((nodo.derecho, nivel + 1))

    return altura


def verificarAVL(arbol):
    def revisar(nodo, limiteInferior=None, limiteSuperior=None):
        if nodo is None:
            return 0

        titulo = nodo.videojuego.titulo.lower()

        if limiteInferior is not None:
            assert titulo > limiteInferior, "Orden incorrecto"

        if limiteSuperior is not None:
            assert titulo < limiteSuperior, "Orden incorrecto"

        alturaIzquierda = revisar(
            nodo.izquierdo, limiteInferior, titulo
        )
        alturaDerecha = revisar(
            nodo.derecho, titulo, limiteSuperior
        )

        alturaReal = 1 + max(alturaIzquierda, alturaDerecha)

        assert nodo.altura == alturaReal, (
            "Altura guardada incorrecta"
        )
        assert abs(alturaIzquierda - alturaDerecha) <= 1, (
            f"Nodo desbalanceado: {nodo.videojuego.titulo}"
        )

        return alturaReal

    revisar(arbol.raiz)


def contarNodosVisitados(arbol, tituloBuscado):
    nodo = arbol.raiz
    tituloBuscado = tituloBuscado.lower()
    visitados = 0

    while nodo is not None:
        visitados += 1
        tituloActual = nodo.videojuego.titulo.lower()

        if tituloBuscado == tituloActual:
            return visitados

        if tituloBuscado < tituloActual:
            nodo = nodo.izquierdo
        else:
            nodo = nodo.derecho

    return visitados


def medirBusqueda(arbol, titulos):
    def buscarTodos():
        for titulo in titulos:
            arbol.buscar(titulo)

    repeticiones = 100

    tiempos = repeat(
        buscarTodos,
        number=repeticiones,
        repeat=5
    )

    # Mediana de cinco mediciones, en microsegundos por búsqueda.
    tiempoMediano = sorted(tiempos)[2]

    return (
        tiempoMediano / (repeticiones * len(titulos))
    ) * 1_000_000


def compararBusquedas(bst, avl, videojuegos):
    titulos = [videojuego.titulo for videojuego in videojuegos]

    # Comprobamos todos los títulos y el uso de mayúsculas.
    for videojuego in videojuegos:
        for titulo in (videojuego.titulo, videojuego.titulo.upper()):
            assert bst.buscar(titulo) is videojuego, (
                f"Error de búsqueda BST: {titulo}"
            )
            assert avl.buscar(titulo) is videojuego, (
                f"Error de búsqueda AVL: {titulo}"
            )

    tituloInexistente = "~~~ VIDEOJUEGO INEXISTENTE ~~~"

    assert tituloInexistente.lower() not in {
        titulo.lower() for titulo in titulos
    }
    assert bst.buscar(tituloInexistente) is None
    assert avl.buscar(tituloInexistente) is None

    # Insertar un título repetido debe devolver False.
    assert bst.insertar(videojuegos[0]) is False
    assert avl.insertar(videojuegos[0]) is False
    verificarAVL(avl)

    print("Búsquedas y rechazo de duplicados: correctos")

    nodosBST = [
        contarNodosVisitados(bst, titulo) for titulo in titulos
    ]
    nodosAVL = [
        contarNodosVisitados(avl, titulo) for titulo in titulos
    ]

    print(
        f"BST: promedio de {sum(nodosBST) / len(nodosBST):.2f} "
        f"nodos visitados; máximo {max(nodosBST)}"
    )
    print(
        f"AVL: promedio de {sum(nodosAVL) / len(nodosAVL):.2f} "
        f"nodos visitados; máximo {max(nodosAVL)}"
    )

    print(
        "Búsqueda inexistente — nodos visitados: "
        f"BST {contarNodosVisitados(bst, tituloInexistente)}, "
        f"AVL {contarNodosVisitados(avl, tituloInexistente)}"
    )

    print(
        f"BST: {medirBusqueda(bst, titulos):.3f} "
        "microsegundos por búsqueda"
    )
    print(
        f"AVL: {medirBusqueda(avl, titulos):.3f} "
        "microsegundos por búsqueda"
    )


def probarOrden(nombre, videojuegos):
    bst = ArbolVideojuegos()
    avl = AVLVideojuegos()

    insertadosBST = 0
    insertadosAVL = 0

    for videojuego in videojuegos:
        if bst.insertar(videojuego):
            insertadosBST += 1

        if avl.insertar(videojuego):
            insertadosAVL += 1

    print(f"\nOrden: {nombre}")
    print(
        f"BST: {insertadosBST} videojuegos, "
        f"altura de {calcularAltura(bst.raiz)} niveles"
    )
    print(
        f"AVL: {insertadosAVL} videojuegos, "
        f"altura de {calcularAltura(avl.raiz)} niveles"
    )

    verificarAVL(avl)
    print("Equilibrio y alturas del AVL: correctos")

    compararBusquedas(bst, avl, videojuegos)


def main():
    ruta = Path(__file__).with_name("videojuegos.json")

    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)

    videojuegos = [
        SimpleNamespace(**dato) for dato in datos
    ]

    ordenados = sorted(
        videojuegos,
        key=lambda videojuego: videojuego.titulo.lower()
    )

    probarOrden("original", videojuegos)
    probarOrden("alfabético ascendente", ordenados)
    probarOrden(
        "alfabético descendente",
        list(reversed(ordenados))
    )


if __name__ == "__main__":
    main()