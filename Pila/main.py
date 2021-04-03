'''
Pila

Una pila es una lista ordenada o estructura de datos en la que el modo de acceso a sus elementos es de tipo 'LIFO' (Last in First Out, Ultimo en Entrar es el Primero en Salir) que permite almacenar datos.

Para el manejo de los datos se cuenta con dos operaciones basicas: apilar(push), que coloca un objeto en la pila, y su opeacion inversa, retirar(o desapilar, pop), que retira el ultimo elemento apilado.

OPERACIONES:
Crear: Se crea una pila vacia (constructor)
Tamaño: Regresa el numero de elementos de la pila (size)
Apilar: Se añade un elemento a la pila (push)
Desapilar: Se elimina el elemento frontal de la pila (pop)
Cima: Devuelve el elemento que esta en la cima de la pila (top o peek)
Vacia: Devuelve True si la pila esta sin elementos o False en caso de que contenga alguno (empty)

Las pilas pueden ser de tamaño estatico y dinamico, se pueden implementar en listas, arreglos, colecciones de datos o el listas enlazadas
'''

from Pila import Pila

pila = Pila(5)

pila.push(25)
pila.push(12)
pila.push(57)

pila.show()
print(pila.top())
