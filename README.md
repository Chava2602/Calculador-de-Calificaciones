## Calculador de calificaciones

Mediante un pequeño código en python se podrá obtener una lista para obtener un promedio final deseado dependiendo del numero de materias y claramente el promedio deseado.

### Funcionamiento

- #### Librerías
    ```python
    import itertools
    ```
    _Itertool_ es un módulo que proporciona varias funciones que funcionan en iteradores para producir iteradores complejos. 

    ```python
    import statistics
    ```
    _statistics_ agrupa un conjunto de funciones para cálculo estadístico.

- #### Inputs
    ```python
    prom = int(input(f'Promedio deseado:\n'))
    ```
    __prom__ es usado para pedir al usuario el promedio deseado.

    ```python
    materias = int(input(f'Materias tomadas:\n'))
    ```
    __materias__ es la variable donde se guarda el numero de materias que se esta cursando donde se utiliza para opener el promedio.

- #### Lista
    ```python
    lst = []
    ```
    Creación de la lista donde se guardaran los números del 60 al 100. 

- #### Condicionales
    ```python
    if prom >= 100:
    print('Ingresa un promedio no mayor a 100')

    elif prom < 60:
    print('No ingresar un promedio menor a 60')
    ```
    Básicamente es una condición si el usuario pune un numero mayor a 100 o menor a 60 soltara un mensaje de erro por asi decirlo.

- #### Generar lista
    ```python
    else:
    for x in range(60, 101):
        lst.append(x)
    ```
    El _for_ es usado para generar una lista de números del 60 al 100.

- #### Combinaciones
    ```python
    lstcali = itertools.combinations(lst, materias)
    ```
    _Itertools.combinations()_ devuelve r subsecuencias de longitud de elementos de la entrada iterable.
    _lst_ es refrente a la lista donde va generar las combinaciones.
    _materias_ va ser el numero de elementos que va mostrar por listas:
    _[0, 1, 2, 3], [0, 1], [0, 1, 2, 3, 4]_

- #### Recorrido de la lista
    ```python
    for i in list(lstcali):
        lsti = list(i)
    ```
    Lo que hace este for va recorriendo cada lista generada por las combinaciones pasadas para pasar al siguiente paso.

- #### Promedio
    ```python
    mean = statistics.mean(lsti)
    ```
    Lo que hace _statistics.mean()_ es sacar el promedio de cada lista generada.

- #### Condicional 2
    ```python
    if mean == prom:
        print(lsti)
    ```
    Por ultimo si el promedio de las listas generadas es igual al promedio deseado mostrara una por una cada lista que conocida con el promedio.
