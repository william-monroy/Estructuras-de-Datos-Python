class Cola():

    def __init__(self):
        self.cola = []
        self.size = 0

    def empty(self):
        return len(self.cola) == 0

    def push(self, dato):
        self.cola += [dato]
        self.size += 1

    def pop(self):
        if self.empty():
            print('La cola esta vacia')
        else:
            self.cola = [self.cola[i] for i in range(1, self.size)]
            self.size -= 1

    def show(self):
        n = self.size - 1
        for i in range(self.size-1, 0-1, -1):
            print(f'[{i}] = {self.cola[i]}')

    def size(self):
        return self.size
    
    def top(self):
        return self.cola[-1]