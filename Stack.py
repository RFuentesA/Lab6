from List import *
class Stack():
    
    def __init__(self):
        self.__data = List(None,None)

    def size(self):
        return self.__data.getSize()
        
    def isEmpty(self):
        if self.__data.getSize() == 0:
            return True
        else:
            return False
        
    def push(self, e):
        self.__data.addFirst(e)
        
    def pop(self):
        return self.__data.removeFirst()
        
    def top(self):
        return self.__data.First().getData()

s = Stack()
s.push(2)
s.push(4)
s.push(6)
s.push(8)
s.push(10)

for i in range(s.size()):
    print(s.pop())