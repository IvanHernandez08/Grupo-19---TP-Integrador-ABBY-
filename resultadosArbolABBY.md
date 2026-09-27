# ABBY v2 - Análisis del árbol binario de búsqueda

## Necesidad resuelta:

Para ABBY v2 se incorporó un árbol binario de búsqueda que permite localizar un videojuego por su título. La clave de ordenamiento elegida fue el título normalizado en minúsculas.

La estrategia se integró al programa principal como una búsqueda real para el usuario y se comparó con la búsqueda secuencial utilizada anteriormente.

## Metodología:

Se generaron catálogos de 100, 1.000 y 10.000 videojuegos. En todos los casos se buscó el título ubicado al final del catálogo, lo que representa el peor caso para la búsqueda secuencial.

Para evitar que la inserción ordenada formara un árbol completamente inclinado, los elementos se insertaron comenzando por los puntos medios. De esta manera se obtuvo un árbol equilibrado para estudiar su comportamiento promedio esperado.

Cada búsqueda fue ejecutada 1.000 veces durante 5 rondas y el costo de construcción del árbol se midió por separado del costo de búsqueda.

## Resultados de las cinco ejecuciones:

| Ejecución | Elementos | Construcción (ms) | Secuencial (ms) | Árbol (ms) |
|---:|---:|---:|---:|---:|
| 1 | 100 | 0,525200 | 0,035983 | 0,002577 |
| 1 | 1.000 | 4,860300 | 0,352590 | 0,004355 |
| 1 | 10.000 | 74,124100 | 3,499037 | 0,005809 |
| 2 | 100 | 0,331900 | 0,035086 | 0,003086 |
| 2 | 1.000 | 3,914300 | 0,319712 | 0,004932 |
| 2 | 10.000 | 54,196700 | 3,568570 | 0,006377 |
| 3 | 100 | 0,466900 | 0,039245 | 0,003137 |
| 3 | 1.000 | 6,864800 | 0,396545 | 0,003996 |
| 3 | 10.000 | 65,779200 | 3,858772 | 0,005777 |
| 4 | 100 | 0,906500 | 0,044085 | 0,002967 |
| 4 | 1.000 | 5,223800 | 0,402280 | 0,004703 |
| 4 | 10.000 | 83,743400 | 3,762719 | 0,005571 |
| 5 | 100 | 0,450300 | 0,041266 | 0,002419 |
| 5 | 1.000 | 4,695100 | 0,346979 | 0,003230 |
| 5 | 10.000 | 65,930800 | 3,649311 | 0,005277 |

## Tabla consolidada:

| Elementos | Construcción promedio (ms) | Secuencial promedio (ms) | Árbol promedio (ms) | Ventaja del árbol |
|---:|---:|---:|---:|---:|
| 100 | 0,536160 | 0,039133 | 0,002837 | 13,79 veces |
| 1.000 | 5,111660 | 0,363621 | 0,004243 | 85,70 veces |
| 10.000 | 68,754840 | 3,667682 | 0,005762 | 636,51 veces |

## Resultados:

La búsqueda secuencial aumentó casi en la misma proporción que el tamaño del catálogo. Al pasar de 100 a 10.000 elementos, el conjunto de datos creció 100 veces y el tiempo secuencial pasó de 0,039133 ms a 3,667682 ms.

La búsqueda en el árbol creció mucho más lentamente. Para 100 elementos demoró en promedio 0,002837 ms y para 10.000 elementos solamente 0,005762 ms. Aunque el catálogo aumentó 100 veces, el tiempo de búsqueda apenas llegó aproximadamente al doble.

El árbol redujo el tiempo de búsqueda aproximadamente un 92,75 % con 100 elementos, un 98,83 % con 1.000 elementos y un 99,84 % con 10.000 elementos.

## Costo inicial y punto de recuperación:

Construir el árbol tiene un costo inicial, pero ABBY lo construye una sola vez al cargar el catálogo y luego lo reutiliza en todas las búsquedas.

Al comparar el costo de construcción con el tiempo ahorrado en cada búsqueda, el costo inicial se recupera aproximadamente después de:

| Elementos | Búsquedas aproximadas para recuperar la construcción |
|---:|---:|
| 100 | 15 búsquedas |
| 1.000 | 15 búsquedas |
| 10.000 | 19 búsquedas |

Por lo tanto, si ABBY realiza búsquedas frecuentes, el costo inicial queda compensado rápidamente. Para una única búsqueda aislada, recorrer directamente la lista podría resultar más económico porque no exige construir una estructura adicional.

## Complejidad algorítmica:

### Búsqueda secuencial

- Mejor caso: `Ω(1)`, cuando el título está al comienzo.
- Caso promedio: `Θ(n)`.
- Peor caso: `O(n)`, cuando el título está al final o no existe.

### Árbol binario de búsqueda equilibrado

- Mejor caso: `Ω(1)`, cuando el título está en la raíz.
- Caso promedio: `Θ(log n)`.
- Peor caso de un árbol equilibrado: `O(log n)`.

### Árbol binario de búsqueda desequilibrado

El árbol implementado no se balancea automáticamente. Si los títulos se insertan ya ordenados, puede quedar inclinado y comportarse como una lista:

- Búsqueda en el peor caso: `O(n)`.
- Inserción en el peor caso: `O(n)` por elemento.

### Otras operaciones

- Inserción en un árbol equilibrado: `Θ(log n)` por elemento.
- Construcción mediante inserciones equilibradas: `Θ(n log n)`.
- Recorrido inorden: `Θ(n)`.
- Recorrido preorden: `Θ(n)`.
- Recorrido postorden: `Θ(n)`.

Los tres recorridos deben visitar todos los nodos, por lo que su complejidad es lineal independientemente del orden utilizado.

## Conclusión técnica:

Los resultados experimentales coinciden con el análisis teórico. La búsqueda secuencial es simple y adecuada para catálogos pequeños o consultas aisladas, pero su tiempo aumenta proporcionalmente con la cantidad de videojuegos.

El árbol binario equilibrado requiere un costo inicial de construcción y memoria adicional, pero permite realizar búsquedas mucho más rápidas. Con 10.000 elementos fue aproximadamente 636 veces más rápido que la búsqueda secuencial y el costo de construcción se recuperó después de unas 19 búsquedas.

Para ABBY v2 resulta conveniente utilizar el árbol cuando el catálogo permanece cargado y se realizan múltiples búsquedas por título. Sin embargo, debe considerarse que el árbol desarrollado no es autoequilibrado: su eficiencia depende del orden de inserción. Una mejora futura sería implementar un árbol AVL o rojinegro para mantener automáticamente una altura cercana a `log n`.
