from time import perf_counter_ns
from statistics import median


def generar_catalogo(cantidad):
    catalogo = []

    for numero in range(cantidad):
        videojuego = {
            "titulo": f"Videojuego {numero:06d}"
        }

        catalogo.append(videojuego)

    return catalogo


def busqueda_secuencial(catalogo, titulo_buscado):
    for videojuego in catalogo:
        if videojuego["titulo"] == titulo_buscado:
            return videojuego

    return None


def busqueda_binaria(catalogo, titulo_buscado):
    izquierda = 0
    derecha = len(catalogo) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        titulo_medio = catalogo[medio]["titulo"]

        if titulo_medio == titulo_buscado:
            return catalogo[medio]

        elif titulo_buscado < titulo_medio:
            derecha = medio - 1

        else:
            izquierda = medio + 1

    return None


def medir_tiempo(
    funcion_busqueda,
    catalogo,
    titulo_buscado,
    repeticiones=1000,
    rondas=5
):
    tiempos = []

    for _ in range(rondas):
        inicio = perf_counter_ns()

        for _ in range(repeticiones):
            resultado = funcion_busqueda(
                catalogo,
                titulo_buscado
            )

        fin = perf_counter_ns()

        if resultado is None:
            raise ValueError(
                "El videojuego utilizado para la prueba no fue encontrado."
            )

        tiempo_promedio_ns = (
            fin - inicio
        ) / repeticiones

        tiempo_promedio_ms = tiempo_promedio_ns / 1_000_000
        tiempos.append(tiempo_promedio_ms)

    return median(tiempos)


def ejecutar_experimentos():
    tamanios = [100, 1000, 10000]
    resultados = []

    print("\nEXPERIMENTO DE COMPLEJIDAD - ABBY")
    print("Búsqueda de un videojuego por título")
    print("Caso analizado: videojuego ubicado al final\n")

    for cantidad in tamanios:
        catalogo = generar_catalogo(cantidad)

        titulo_buscado = (
            f"Videojuego {cantidad - 1:06d}"
        )

        resultado_secuencial = busqueda_secuencial(
            catalogo,
            titulo_buscado
        )

        resultado_binario = busqueda_binaria(
            catalogo,
            titulo_buscado
        )

        if resultado_secuencial != resultado_binario:
            raise ValueError(
                "Las estrategias devolvieron resultados diferentes."
            )

        tiempo_secuencial = medir_tiempo(
            busqueda_secuencial,
            catalogo,
            titulo_buscado
        )

        tiempo_binario = medir_tiempo(
            busqueda_binaria,
            catalogo,
            titulo_buscado
        )

        resultados.append(
            (
                cantidad,
                tiempo_secuencial,
                tiempo_binario
            )
        )

    print(
        f"{'Elementos':>12} | "
        f"{'Secuencial (ms)':>17} | "
        f"{'Binaria (ms)':>15}"
    )

    print("-" * 52)

    for cantidad, secuencial, binaria in resultados:
        print(
            f"{cantidad:>12} | "
            f"{secuencial:>17.6f} | "
            f"{binaria:>15.6f}"
        )


if __name__ == "__main__":
    ejecutar_experimentos()