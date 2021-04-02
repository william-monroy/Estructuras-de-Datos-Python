'''
Metodo de Ordenamiento Burbuja

Revisa cada elemento de la lista con el siguiente elemento, intercambiando de posicion si estan en el orden incorrecto

Ejemplo:

4 2 6 8 5 7
2 4 6 8 5 7
2 4 6 5 8 7
2 4 6 5 7 8
2 4 5 6 7 8
'''

lista = [4,2,6,8,5,7]

aux = 0
for i in range(len(lista)):
    for j in range(len(lista)-1):
        if lista[j] > lista[j+1]:
            aux=lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux
            print(lista)