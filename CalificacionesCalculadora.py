import itertools
import statistics

prom = int(input(f'Promedio deseado:\n'))

materias = int(input(f'Materias tomadas:\n'))

lst = []

while True:

    if prom >= 100:
        print('Ingresa un promedio no mayor a 100')

    elif prom < 60:
        print('No ingresar un promedio menor a 60')
        
    else:
        for x in range(60, 101):
            lst.append(x)
            
        prome = itertools.combinations(lst, materias)
        for i in list(prome):
            lsti = list(i)
            mean = statistics.mean(lsti)
            if mean == prom:
                print(lsti)

    input('Pulsa ENTER para continuar...')
    break