'''
Ordenamiento por Seleccion

Funcionamiento:
- Buscar el dato mas pequeño de la lista
- Intercambiarlo por el actual
- Seguir buscando el dato mas pequeño de la lista
- Intercambiarlo por el actual
- Esto se repetira sucesivamente
'''

lista = [4,2,6,8,5,7,0]

for i in range(len(lista)):
    minimo = i
    for j in range(i,len(lista)):
        if lista[j] < lista[minimo]:
            minimo = j
    aux = lista[i]
    lista[i] = lista[minimo]
    lista[minimo] = aux

print(lista)