# ABBY v2 - Recomendador de videojuegos

ABBY es una aplicación de terminal desarrollada en Python que permite consultar un catálogo de videojuegos cargado desde un archivo JSON.

## Funcionalidades

1. Buscar videojuegos por género.
2. Consultar hasta 20 videojuegos de una consola o plataforma, ordenados por calificación.
3. Buscar un videojuego por su título completo mediante un árbol binario de búsqueda.

El catálogo incluye el título, el desarrollador, los géneros, las plataformas y las calificaciones de cada videojuego.

## Árbol binario de búsqueda

La versión 2 incorpora un árbol binario de búsqueda ordenado alfabéticamente por título que permite:

- Insertar videojuegos.
- Buscar un título sin distinguir entre mayúsculas y minúsculas.
- Recorrer el árbol en inorden, preorden y postorden.

La búsqueda por título está integrada en la opción `3` del programa principal. El título debe escribirse completo.

## Estructura del proyecto

```text
Project ABBY/
├── Proyect ABBY.py
├── arbolVideojuegos.py
├── pruebasArbolABBY.py
├── experimentosABBY.py
├── experimentosArbolABBY.py
├── videojuegos.json
├── resultadosComplejidadABBY.md
├── resultadosArbolABBY.md
└── README.md
```

- `Proyect ABBY.py`: aplicación principal e interfaz de terminal.
- `arbolVideojuegos.py`: implementación del árbol binario de búsqueda.
- `pruebasArbolABBY.py`: pruebas de inserción, búsqueda y recorridos.
- `experimentosABBY.py`: comparación de búsqueda secuencial y binaria de la entrega 2.
- `experimentosArbolABBY.py`: comparación de búsqueda secuencial y búsqueda en árbol.
- `videojuegos.json`: catálogo y datos de prueba.
- `resultadosComplejidadABBY.md`: resultados de la entrega 2.
- `resultadosArbolABBY.md`: resultados y análisis de complejidad de la entrega 3.

## Requisitos

- Python 3.10 o posterior.
- No requiere instalar librerías externas.

## Ejecución de ABBY v2

1. Descargar o clonar el repositorio.
2. Verificar que `Proyect ABBY.py`, `arbolVideojuegos.py` y `videojuegos.json` estén en la misma carpeta.
3. Abrir una terminal en esa carpeta.
4. Ejecutar el comando: 

    python "Proyect ABBY.py" 

-Nota: En algunos equipos el comando puede ser: python3 "Proyect ABBY.py"

-Aclaración: Las comillas son necesarias porque el nombre del archivo contiene un espacio.
## Uso

El menú principal muestra estas opciones:

1. Búsqueda por género
2. Top por consola
3. Búsqueda por título


En la opción `1`, el usuario escribe un género y ABBY muestra los videojuegos relacionados. En la opción `2`, selecciona una plataforma y recibe hasta 20 títulos ordenados por su calificación para esa plataforma. En la opción `3`, escribe el título completo y ABBY lo busca en el árbol binario.

## Pruebas del árbol

Para probar la búsqueda de un título existente, un título inexistente y los tres recorridos, ejecutar: python pruebasArbolABBY.py


El recorrido inorden debe mostrar los títulos en orden alfabético.

## Experimento de complejidad

Para comparar la búsqueda secuencial con la búsqueda en árbol usando catálogos de 100, 1.000 y 10.000 elementos, ejecutar:
python experimentosArbolABBY.py


El experimento también mide por separado el costo de construcción del árbol. La metodología, las tablas y la conclusión técnica se encuentran en `resultadosArbolABBY.md`.

## Complejidad

- Búsqueda secuencial: `Θ(n)` en el caso promedio.
- Búsqueda en un árbol equilibrado: `Θ(log n)` en el caso promedio.
- Búsqueda en un árbol completamente desequilibrado: `O(n)` en el peor caso.
- Recorridos inorden, preorden y postorden: `Θ(n)`.

El árbol implementado no se balancea automáticamente, por lo que su rendimiento depende del orden de inserción.

## Tecnologías utilizadas

- Python
- JSON
- Git y GitHub

## Fuente de los datos

Las calificaciones utilizadas corresponden a Metascores de críticos publicados por Metacritic. Los valores pueden variar si la fuente incorpora o modifica reseñas.
