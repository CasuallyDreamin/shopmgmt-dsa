from dll import dll

class queue:
    def __init__(self):
       self.list = dll()

    def enqueue(self, data):
        self.list.add_last(data)

    def dequeue(self):
        data = self.list.get_first()
        self.list.remove_first()
        return data
    
    def get_all(self):
        return self.list.get_all_arr()
      