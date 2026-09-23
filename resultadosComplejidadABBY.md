# ABBY - Análisis de complejidad

## Operación analizada:

La operación elegida fue la búsqueda de un videojuego por su título, opción que actualmente no existe dentro de ABBY pero nos pareció que de este modo iba a ser más fácil el análisis. Por lo que implementamos y comparamos dos estrategias que devuelven el mismo resultado:

1. Búsqueda secuencial.
2. Búsqueda binaria.

Para representar el peor caso de la búsqueda secuencial, en todos los experimentos se buscó el videojuego ubicado al final del catálogo.

## Metodología:

Se generaron catálogos ordenados de 100, 1.000 y 10.000 videojuegos. Para reducir el efecto de variaciones circunstanciales del equipo, cada medición interna se repitió 1.000 veces durante 5 rondas y se tomó la mediana. Además, ejecutamos el experimento completo 5 veces.

La generación del catálogo no fue incluida en los tiempos: medimos únicamente la operación de búsqueda.

## Resultados de las cinco ejecuciones:

| Ejecución | Elementos | Secuencial (ms) | Binaria (ms) |
|---:|---:|---:|---:|
| 1 | 100 | 0,012485 | 0,002582 |
| 1 | 1.000 | 0,133729 | 0,004480 |
| 1 | 10.000 | 1,357752 | 0,006162 |
| 2 | 100 | 0,013397 | 0,003325 |
| 2 | 1.000 | 0,127358 | 0,005208 |
| 2 | 10.000 | 1,317761 | 0,006014 |
| 3 | 100 | 0,015277 | 0,002993 |
| 3 | 1.000 | 0,124792 | 0,004448 |
| 3 | 10.000 | 1,296110 | 0,006327 |
| 4 | 100 | 0,013666 | 0,003010 |
| 4 | 1.000 | 0,128201 | 0,005251 |
| 4 | 10.000 | 1,491224 | 0,006233 |
| 5 | 100 | 0,012967 | 0,003213 |
| 5 | 1.000 | 0,134801 | 0,004581 |
| 5 | 10.000 | 1,450025 | 0,006640 |

## Resumen:

| Elementos | Secuencial promedio (ms) | Binaria promedio (ms) | Ventaja de la binaria |
|---:|---:|---:|---:|
| 100 | 0,013558 | 0,003025 | 4,48 veces |
| 1.000 | 0,129776 | 0,004794 | 27,07 veces |
| 10.000 | 1,382574 | 0,006275 | 220,32 veces |

## Análisis de los resultados:

Al pasar de 100 a 1.000 elementos, la entrada se multiplicó por 10 y el tiempo secuencial se multiplicó aproximadamente por 9,57. Al pasar de 1.000 a 10.000 elementos, volvió a multiplicarse por 10 y el tiempo secuencial aumentó aproximadamente 10,65 veces. Esto coincide con un crecimiento lineal.

En cambio, el tiempo de la búsqueda binaria pasó de 0,003025 ms con 100 elementos a solamente 0,006275 ms con 10.000 elementos. Aunque el catálogo se hizo 100 veces más grande, su tiempo apenas llegó a duplicarse.

La búsqueda binaria redujo el tiempo promedio aproximadamente un 77,69 % con 100 elementos, un 96,31 % con 1.000 elementos y un 99,55 % con 10.000 elementos.

Las pequeñas diferencias entre las cinco ejecuciones son normales y pueden ser causadas por procesos en segundo plano, uso del procesador, administración de memoria y tareas propias del PyCharm. Por lo que ninguna variación cambia la tendencia general observada.

## Análisis de complejidad:

### Búsqueda secuencial

La búsqueda secuencial revisa los videojuegos uno por uno desde el inicio del catálogo.

- Mejor caso, `Ω(1)`: el título buscado está en la primera posición.
- Peor caso, `O(n)`: el título está al final o no existe.
- Caso promedio, `Θ(n)`: la cantidad de elementos revisados crece de manera proporcional al tamaño del catálogo.

### Búsqueda binaria

La búsqueda binaria compara el título con el elemento central y descarta la mitad restante en cada paso.

- Mejor caso, `Ω(1)`: el título está en la posición central.
- Peor caso, `O(log n)`: en cada comparación se elimina la mitad del espacio de búsqueda.
- Caso promedio, `Θ(log n)`.

Esta estrategia requiere que el catálogo esté ordenado por título. Ordenarlo inicialmente tiene un costo de `Θ(n log n)`, pero luego cada búsqueda requiere solamente `Θ(log n)`. En el experimento, el catálogo ya estaba ordenado y el tiempo de preparación no se incluyó en la medición.

## Conclusión:

La búsqueda secuencial es sencilla y puede ser suficiente para un catálogo pequeño o para realizar una única búsqueda sobre datos desordenados. Sin embargo, su tiempo aumenta de manera proporcional a la cantidad de videojuegos.

Por lo que La búsqueda binaria resulta ser la mejor opción para ABBY cuando el catálogo está ordenado y se realizan búsquedas frecuentes. Su ventaja aumenta a medida que crece el conjunto de datos: con 10.000 elementos fue aproximadamente 220 veces más rápida que la búsqueda secuencial.

Por lo tanto, para un catálogo grande y ordenado se recomienda utilizar búsqueda binaria. Pero si los datos no estuvieran ordenados y solamente se necesitara una búsqueda ocasional, habría que considerar también el costo inicial de ordenamiento antes de elegirla.
