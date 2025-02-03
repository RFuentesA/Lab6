class Usuario():
    def __init__(self, nombre, id):
        self.__nombre = nombre
        self.__id = id
    
    def Usuario(self):
        self.__init__()
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id
    
    def __str__(self):
        return "El Nombre del usuario es: " + str(self.__nombre) + " identificado con el id: " + str(self.__id)

#us1 = Usuario("Ricardo", 1234)
#print(us1)