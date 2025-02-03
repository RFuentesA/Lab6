from List import *

class Queue():
    def __init__(self):
        self.__data = List(None,None)
        
    def size(self):
        return self.__data.getSize()
    
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
        return self.__data.removeFirst()
    
    
"""q = Queue()
q.enqueue(2)
q.enqueue(4)
q.enqueue(6)
q.enqueue(8)
q.enqueue(10)
q.enqueue(12)

for i in range(q.size()):
    print(q.dequeue())"""