# ABBY - Recomendador de videojuegos

ABBY es nuestra aplicación de terminal que permite consultar un catálogo de videojuegos de dos maneras:

1. Buscar videojuegos por género.
2. Consultar el top 20 de videojuegos de una consola o plataforma. (aunque algunas no llegan a 20)

El catálogo se carga desde un archivo JSON y contiene información como:\
-Título\
-Desarrollador \
-Géneros\
-Plataformas\
-Calificaciones de Metacritic.

## Funcionalidades

- Carga de datos desde un archivo JSON.
- Búsqueda y filtrado de videojuegos por género.
- Listado del top 20 (o menos en algunos casos) por consola o plataforma.
- Ordenamiento según la calificación correspondiente a la plataforma seleccionada.
- Validación de las opciones ingresadas por el usuario.
- Uso de clases, objetos y encapsulamiento.

## Estructura del proyecto

- `Proyect ABBY.py`: contiene las clases, la lógica de búsqueda y la interfaz de terminal.
- `videojuegos.json`: contiene el catálogo y los datos de prueba utilizados por la aplicación.
- `README.md`: contiene la descripción y las instrucciones del proyecto.

## Instrucciones de ejecución

1. Descargar o clonar este repositorio.
2. Verificar que `Proyect ABBY.py` y `videojuegos.json` estén dentro de la misma carpeta.
3. Abrir una terminal en la carpeta del proyecto.
4. Ejecutar el comando: 

    python "Proyect ABBY.py"

    -Nota: En algunos equipos el comando puede ser: python3 "Proyect ABBY.py"

-Aclaración: Las comillas son necesarias porque el nombre del archivo contiene un espacio.

## Uso

Al iniciar el programa se muestran dos opciones luego del saludo inicial:

1. Búsqueda por género
2. Top por consola


### Búsqueda por género

El usuario selecciona la opción `1` e ingresa un género, por ejemplo:

```text
RPG
```

ABBY muestra los videojuegos relacionados con ese género junto con su desarrollador, plataformas y calificación.

### Top por consola

El usuario selecciona la opción `2`, elige una plataforma de la lista y ABBY muestra hasta 20 videojuegos ordenados por su Metascore específico para esa plataforma.

## Datos de prueba

Los datos de prueba se encuentran en `videojuegos.json`. Este archivo contiene el catálogo utilizado para comprobar las búsquedas por género y los rankings por plataforma.

Algunas pruebas sugeridas son:

| Prueba | Entrada   | Resultado esperado                                                       |
|---|-----------|--------------------------------------------------------------------------|
| Opción principal inválida | `3`       | El programa informa que solo `1` y `2` son válidas y vuelve a preguntar. |
| Búsqueda por género | `RPG`     | Muestra los videojuegos correspondientes al género RPG.                  |
| Género inexistente | `Musical` | Informa que no encontró resultados y vuelve a preguntar.                 |
| Top por consola | `1`       | Muestra el top de PlayStation 5.                                         |
| Consola inválida | `23`      | Informa que se debe ingresar un número entre `1` y `17`.                 |

## Demo de la versión 1

La demostración en video debe mostrar, como mínimo:

1. El inicio de ABBY.
2. La validación de una opción incorrecta.
3. Una búsqueda por género.
4. Una consulta del top por consola.

Enlace al video de demostración: 

    Drive: https://drive.google.com/file/d/17Hcvlf6j6iccO0tkjjI-xRkWLb545YsK/view?usp=sharing
    YT: https://youtu.be/-H-UmdbV8MM

## Tecnologías utilizadas

- Python
- JSON
- Git y GitHub

## Fuente de los datos

Las calificaciones utilizadas corresponden a Metascores de críticos publicados por Metacritic. Los valores pueden variar si la fuente incorpora o modifica reseñas.
