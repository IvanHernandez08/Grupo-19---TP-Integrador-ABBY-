from time import perf_counter_ns
from statistics import median

from arbolVideojuegos import ArbolVideojuegos


class VideojuegoPrueba:
    def __init__(self, titulo):
        self.titulo = titulo


def generarCatalogo(cantidad):
    catalogo = []

    for numero in range(cantidad):
        videojuego = VideojuegoPrueba(
            f"Videojuego {numero:06d}"
        )
        catalogo.append(videojuego)

    return catalogo


def busquedaSecuencial(catalogo, tituloBuscado):
    for videojuego in catalogo:
        if videojuego.titulo.lower() == tituloBuscado.lower():
            return videojuego

    return None


def insertarBalanceado(arbol, catalogo, inicio, final):
    if inicio > final:
        return

    posicionMedia = (inicio + final) // 2

    arbol.insertar(catalogo[posicionMedia])

    insertarBalanceado(
        arbol,
        catalogo,
        inicio,
        posicionMedia - 1
    )

    insertarBalanceado(
        arbol,
        catalogo,
        posicionMedia + 1,
        final
    )


def construirArbolBalanceado(catalogo):
    arbol = ArbolVideojuegos()

    insertarBalanceado(
        arbol,
        catalogo,
        0,
        len(catalogo) - 1
    )

    return arbol


def medirTiempo(
    funcionBusqueda,
    estructura,
    tituloBuscado,
    repeticiones=1000,
    rondas=5
):
    tiempos = []

    for _ in range(rondas):
        inicio = perf_counter_ns()

        for _ in range(repeticiones):
            resultado = funcionBusqueda(
                estructura,
                tituloBuscado
            )

        final = perf_counter_ns()

        if resultado is None:
            raise ValueError(
                "El videojuego de prueba no fue encontrado."
            )

        tiempoPromedioNanosegundos = (
            final - inicio
        ) / repeticiones

        tiempoPromedioMilisegundos = (
            tiempoPromedioNanosegundos / 1_000_000
        )

        tiempos.append(tiempoPromedioMilisegundos)

    return median(tiempos)


def buscarEnArbol(arbol, tituloBuscado):
    return arbol.buscar(tituloBuscado)


def ejecutarExperimentos():
    tamanios = [100, 1000, 10000]
    resultados = []

    print("\nCOMPARACIÓN DE ESTRATEGIAS - ABBY V2")
    print("Búsqueda secuencial vs. árbol binario")
    print("Caso analizado: título ubicado al final\n")

    for cantidad in tamanios:
        print(
            f"Procesando catálogo de {cantidad} videojuegos...",
            flush=True
        )

        catalogo = generarCatalogo(cantidad)

        tituloBuscado = (
            f"Videojuego {cantidad - 1:06d}"
        )

        inicioConstruccion = perf_counter_ns()

        arbol = construirArbolBalanceado(catalogo)

        finalConstruccion = perf_counter_ns()

        tiempoConstruccion = (
            finalConstruccion - inicioConstruccion
        ) / 1_000_000

        tiempoSecuencial = medirTiempo(
            busquedaSecuencial,
            catalogo,
            tituloBuscado
        )

        tiempoArbol = medirTiempo(
            buscarEnArbol,
            arbol,
            tituloBuscado
        )

        resultadoSecuencial = busquedaSecuencial(
            catalogo,
            tituloBuscado
        )

        resultadoArbol = arbol.buscar(tituloBuscado)

        if resultadoSecuencial.titulo != resultadoArbol.titulo:
            raise ValueError(
                "Las estrategias devolvieron resultados diferentes."
            )

        resultados.append(
            (
                cantidad,
                tiempoConstruccion,
                tiempoSecuencial,
                tiempoArbol
            )
        )

        print(
            f"Prueba de {cantidad} videojuegos terminada.\n",
            flush=True
        )

    print(
        f"{'Elementos':>10} | "
        f"{'Construcción (ms)':>17} | "
        f"{'Secuencial (ms)':>16} | "
        f"{'Árbol (ms)':>12}"
    )

    print("-" * 66)

    for (
        cantidad,
        construccion,
        secuencial,
        arbol
    ) in resultados:
        print(
            f"{cantidad:>10} | "
            f"{construccion:>17.6f} | "
            f"{secuencial:>16.6f} | "
            f"{arbol:>12.6f}"
        )


if __name__ == "__main__":
    ejecutarExperimentos()