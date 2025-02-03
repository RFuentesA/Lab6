from List import*

class Queue():
    def __init__(self):
        self.__data = List(None,None)
        
    def size(self):
        self.__data.getSize()
    
    def isEmpty(self):
        if self.__data.getSize() == 0:
            return True
        else:
            return False
    
    def first(self):
        return self.__data.First().getData()
    
    def enqueue(self, e):
        self.__data.addLast(e)
    
    def dequeue(self):
        print(self.__data.removeFirst())

q = Queue()
q.enqueue(2)
q.enqueue(4)
q.enqueue(6)
q.enqueue(8)
q.enqueue(10)

for i in range(5):
    q.dequeue()