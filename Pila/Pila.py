class Pila():

    def __init__(self, size):
        self.lista = []
        self.tope = 0
        self.size = size

    def empty(self):
        if self.tope == 0:
            return True
        else:
            return False

    def push(self, dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1
        else:
            # Dinamica
            self.size += 5
            self.lista += [dato]
            self.tope += 1
            # print('La pila esta llena') --> Estatica

    def pop(self):
        if self.empty():
            print('La pila esta vacía')
        else:
            self.tope -= 1
            self.lista = [self.lista[x] for x in range(self.tope)]

    def show(self):
        for i in range(self.tope-1, 0, -1):
            print(f'[{i}] = {self.lista[i]}')

    def size(self):
        return self.tope

    def top(self):
        return self.lista[-1]
