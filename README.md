# ABBY v3 - Recomendador de videojuegos

ABBY es una aplicación de terminal desarrollada en Python que permite consultar un catálogo de videojuegos cargado desde un archivo JSON.

## Funcionalidades

1. Buscar videojuegos por género.
2. Consultar hasta 20 videojuegos de una consola o plataforma, ordenados por calificación.
3. Buscar un videojuego por su título completo mediante un árbol binario de búsqueda.
4. Explorar categorías mediante un árbol general: plataforma → género → videojuego.

El menú permite volver a realizar consultas y salir con la opción '0'.

El catálogo incluye el título, el desarrollador, los géneros, las plataformas y las calificaciones de cada videojuego.

## Árbol binario de búsqueda

La versión 2 incorpora un árbol binario de búsqueda ordenado alfabéticamente por título que permite:

- Insertar videojuegos.
- Buscar un título sin distinguir entre mayúsculas y minúsculas.
- Recorrer el árbol en inorden, preorden y postorden.

La búsqueda por título está integrada en la opción '3' del programa principal. El título debe escribirse completo.

## Árbol general: novedad de la versión 3

"arbolGeneralABBY.py" organiza el catálogo con la jerarquía: Catálogo ABBY > Plataforma > Género > Videojuego. Cada nodo puede tener varios hijos y un juego puede aparecer en distintas ramas, mediante nodos independientes que referencian el mismo objeto del catálogo.

La implementación incluye construcción automática desde el catálogo, búsqueda exacta de nombres sin distinguir mayúsculas y minúsculas, recorrido en profundidad y recorrido por niveles. La búsqueda devuelve todas las coincidencias con sus rutas.

Actualmente, el catálogo posee 190 videojuegos, 17 plataformas y 602 nodos, contando categorías y apariciones de videojuegos.

## AVL: entrega 4

"avlABBY.py" implementa un árbol AVL con inserción, búsqueda, almacenamiento de alturas y rotaciones simples y dobles mientras que "experimentosDesbalance.py" compara su comportamiento con el BST usando los títulos en orden original, ascendente y descendente.

El AVL se utiliza en los experimentos; la búsqueda por título del menú continúa usando el BST.

## Ejecución de ABBY v3

1. Descargar o clonar el repositorio.
2. Verificar que "Proyect ABBY.py", "arbolVideojuegos.py", "arbolGeneralABBY.py" y "videojuegos.json" estén en la misma carpeta.
3. Abrir una terminal en esa carpeta.
4. Ejecutar:
>> python "Proyect ABBY.py"


-Nota: En algunos equipos se utiliza 'python3' en lugar de 'python'. Las comillas son necesarias porque el nombre contiene un espacio.

## Uso

El menú principal muestra estas opciones:

1. Búsqueda por género
2. Top por consola
3. Búsqueda por título
4. Explorar categorías
0. Salir


En la opción '1', el usuario escribe un género y ABBY muestra los videojuegos relacionados. En la opción '2', selecciona una plataforma y recibe hasta 20 títulos ordenados por su calificación para esa plataforma. En la opción '3', escribe el título completo y ABBY lo busca en el árbol binario.

En la opción '4', se eligen plataforma, género y videojuego mediante opciones numeradas. Las opciones aparecen en orden alfabético. Al abrir un juego se muestran sus datos y la calificación correspondiente a la plataforma elegida. Enter vuelve al género y '0' retrocede un nivel; desde la lista de plataformas, '0' regresa al menú principal. Las entradas inválidas permiten reintentar.

Ejemplo de navegación: 4 > Nintendo 64 > Plataformas > Super Mario 64, seleccionando los números que aparecen en pantalla.

## Pruebas del árbol general


>python arbolGeneralABBY.py

Muestra plataformas, total de nodos, ejemplos de los recorridos en profundidad y por niveles, y la ruta de Super Mario 64. Comprueba que ambos recorridos visitan el mismo conjunto de nodos y que una búsqueda inexistente devuelve una lista vacía. El mensaje final esperado es Pruebas de recorridos y búsqueda: correctas.

## Pruebas y experimentos del AVL


>python avlABBY.py

>python experimentosDesbalance.py


El primer comando prueba las cuatro situaciones de rotación. El segundo utiliza "videojuegos.json" y verifica equilibrio, alturas, búsquedas y rechazo de duplicados, además de comparar alturas, nodos visitados y tiempos de búsqueda con el BST. Los tiempos varían según el equipo y la ejecución.

## Pruebas del árbol

Para probar la búsqueda de un título existente, un título inexistente y los tres recorridos, ejecutar: python pruebasArbolABBY.py


El recorrido inorden debe mostrar los títulos en orden alfabético.

## Experimento de complejidad

Para comparar la búsqueda secuencial con la búsqueda en árbol usando catálogos de 100, 1.000 y 10.000 elementos, ejecutar:
python experimentosArbolABBY.py


El experimento también mide por separado el costo de construcción del árbol. La metodología, las tablas y la conclusión técnica se encuentran en "resultadosArbolABBY.md".

## Complejidad

- Una búsqueda en BST o AVL recorre un camino de altura 'h': 'O(h)'.
- Un BST desbalanceado puede alcanzar altura lineal y búsquedas 'O(n)' en el peor caso.
- El AVL mantiene altura 'O(log n)' y garantiza búsquedas 'O(log n)' en el peor caso.
- Los recorridos del BST visitan sus 'n' nodos: 'Θ(n)'.
- Los recorridos y la búsqueda exhaustiva del árbol general visitan sus 'N' nodos: 'Θ(N)' visitas. 'N' incluye categorías y apariciones de juegos. La creación y almacenamiento de las rutas agrega un costo proporcional a sus longitudes; en esta jerarquía hay como máximo cuatro nodos por ruta.

El BST del menú no se balancea automáticamente. El árbol general representa categorías y su búsqueda recorre la estructura; no aplica la búsqueda binaria del BST.

## Tecnologías utilizadas

- Python
- JSON
- Git y GitHub

## Fuente de los datos

Las calificaciones utilizadas corresponden a Metascores de críticos publicados por Metacritic. Los valores pueden variar si la fuente incorpora o modifica reseñas.
