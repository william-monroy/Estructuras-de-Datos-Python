'''
Busqueda Lineal

Funcionamiento:

- Recorrer cada elemento de la lista
- Ir comparando el elemento que se desea buscar con cada elemento de la lista
- En caso de ser encontrado retornar el indice en el que se encuentra, en caso contrario retornar False, None, etc
'''

lista = [12,45,78,9,6,5,4,2,1,0,12,45,78,63,25,98]

def buscar (bus):
    for i in range(len(lista)):
        if bus == lista[i]:
            return i    
    return None

print(buscar(100))