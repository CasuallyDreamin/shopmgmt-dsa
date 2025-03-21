class arr:
    def __init__(self, size = 10):
        self.size = size
        self.array = size * [None]

    def insert(self, idx:int, data):
        self.array[idx] = data

    def get(self, idx:int):
        return self.array[idx]
        


