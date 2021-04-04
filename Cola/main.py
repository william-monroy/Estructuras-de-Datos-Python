'''
Cola

Es una estructura de datos, caracterizada por ser una secuencia de elementos en la que la operación de insercion (push) se realiza por un extremo y la operacion de extraccion (pop) por el otro. También se le llama estructura FIFO (del inglés First In First Out), debido a que el primer elemento en entrar será también el primero en salir.

OPERACIONES: 
- Insertar
- Eliminar
- Buscar
- Estado de la cola (vacía o con elementos)
- Retornar elemento frontal
- Retornar el tamaño de la cola
- Etc
'''

from Cola import Cola

cola = Cola()

cola.push(12)
cola.push(34)
cola.push(35)
cola.push(17)
cola.push(36)

cola.show()

cola.pop()
print('--------------------------------')
cola.show()