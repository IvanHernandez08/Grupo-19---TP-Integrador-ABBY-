import json
from pathlib import Path
from types import SimpleNamespace

from heapABBY import HeapABBY


class VideojuegoPrueba(SimpleNamespace):
    def obtener_calificacion_por_plataforma(self, plataforma):
        for nombre, puntuacion in getattr(self, "calificaciones", {}).items():
            if nombre.lower() == plataforma.lower():
                return puntuacion

        return self.calificacion


def topConHeap(videojuegos, plataforma, cantidad):
    heap = HeapABBY()
    heap.construir(videojuegos, plataforma)

    return [
        heap.extraerMaximo()
        for _ in range(min(cantidad, heap.cantidad()))
    ]


def main():
    ruta = Path(__file__).with_name("videojuegos.json")

    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)

    catalogo = [
        VideojuegoPrueba(**dato) for dato in datos
    ]

    plataformas = sorted({
        plataforma
        for juego in catalogo
        for plataforma in juego.plataformas
    }, key=str.lower)

    for plataforma in plataformas:
        candidatos = [
            juego for juego in catalogo
            if any(
                nombre.lower() == plataforma.lower()
                for nombre in juego.plataformas
            )
        ]

        esperado = sorted(
            candidatos,
            key=lambda juego: (
                juego.obtener_calificacion_por_plataforma(plataforma)
            ),
            reverse=True
        )

        for cantidad in (1, 5, 20, len(candidatos) + 5):
            obtenido = topConHeap(
                candidatos, plataforma, cantidad
            )

            assert [juego.id for juego in obtenido] == [
                juego.id for juego in esperado[:cantidad]
            ], f"Resultado incorrecto: {plataforma}, Top {cantidad}"

    heapVacio = HeapABBY()
    heapVacio.construir([], "Plataforma de prueba")
    assert heapVacio.extraerMaximo() is None

    # Prueba de inserción después de construir el heap.
    heapDinamico = HeapABBY()

    juegosPrueba = [
        VideojuegoPrueba(
            titulo="Juego A",
            calificacion=80,
            plataformas=["PC"]
        ),
        VideojuegoPrueba(
            titulo="Juego B",
            calificacion=90,
            plataformas=["PC"]
        )
    ]

    heapDinamico.construir(juegosPrueba, "PC")

    juegoNuevo = VideojuegoPrueba(
        titulo="Juego nuevo",
        calificacion=95,
        plataformas=["PC"]
    )

    heapDinamico.insertar(juegoNuevo, 95)

    assert heapDinamico.extraerMaximo().titulo == "Juego nuevo"
    assert heapDinamico.extraerMaximo().titulo == "Juego B"
    assert heapDinamico.extraerMaximo().titulo == "Juego A"

    print("Inserción dinámica: correcta")

    print("Comparación con ordenamiento: correcta")
    print("Heap vacío: correcto")
    print("Todas las pruebas pasaron.")


if __name__ == "__main__":
    main()