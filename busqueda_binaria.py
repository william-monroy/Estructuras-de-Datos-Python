'''
Busqueda bianria

Ventajas:
Realiza menos comparaciones que el metodo de busqueda lineal

Requisitos antes de realizar dicho algoritmo:
Tener la lista ordenada de forma ascendete (MENOR A MAYOR)

Funcionamiento:
- Calcular el punto medio, (izquierda + derecha)/2
- Comparar el punto medio con el dato a Buscar
- Si es igual el dato al punto medio, retornar indice
- Si el dato a buscar es mayor que el punto medio, izquierda es igual al valor del medio + 1
- Si el dato a buscar es menor que el punto medio, derecha es igual al valor del medio - 1
- Se seguira ejecuanto siempre y cuando izquierda sea menor o igual a derecha
'''


def busqueda_bianria(dato):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <=derecha:
        medio = (izquierda+derecha)//2
        if dato == lista[medio]:
            return medio
        elif dato < lista[medio]:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    return None

lista = [5, 12, 15, 30, 50, 65, 70, 87, 88, 96]

print(busqueda_bianria(96))