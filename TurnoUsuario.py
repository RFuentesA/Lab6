from Stack import *
from Queue import *
from Usuario import *

class TurnoUsuario():
    def __init__(self):
        self.__registro = Queue()
        self.__usuariosAtendidos = Stack()

    def TurnoUsuario(self):
        self.__init__()
    
    def getRegistro(self):
        return self.__registro
    
    def getUsuariosAtendidos(self):
        return self.__usuariosAtendidos
    
    def registrar(self, u):
        self.__registro.enqueue(u)
    
    def atenderSiguiente(self):
        self.__usuariosAtendidos.push(self.__registro.dequeue())
    
    def setRegistro(self, q):
        self.__registro = q
    
    def setUsuariosAtendidos(self, s):
        self.__usuariosAtendidos = s
            
    def toFile(self):
        #cola vacia pila vacia
        if self.getRegistro().isEmpty():
            if self.getUsuariosAtendidos().isEmpty():
                print("NO hay nada cachon")
            
            #cola vacia pila llena
            elif self.getUsuariosAtendidos().isEmpty() == False:
                sN1 = Stack()
                sN2 = Stack()
                for i in range(self.getUsuariosAtendidos().size()):
                    temp = self.getUsuariosAtendidos().pop()
                    with open("Textos/UsuariosAtendidos.txt", "a") as archivo:
                        archivo.write(str(temp) + "\n")
                    sN1.push(temp)
                for i in range(sN1.size()):
                    temp2 = sN1.pop()
                    sN2.push(temp2)
                self.setUsuariosAtendidos(sN2)
                
        
        elif self.getRegistro().isEmpty() == False:
            qN1 = Queue()
            for i in range(self.getRegistro().size()):
                temp = self.getRegistro().dequeue()
                with open("Textos/UsuariosPendientes.txt", "a") as archivo:
                    archivo.write(str(temp) + "\n")
                qN1.enqueue(temp)
            self.setRegistro(qN1)
            
            #cola llena pila vacia
            if self.getUsuariosAtendidos().isEmpty():
                pass
            
            #cola llena pila llena
            elif self.getUsuariosAtendidos().isEmpty() == False:
                sN1 = Stack()
                sN2 = Stack()
                for i in range(self.getUsuariosAtendidos().size()):
                    temp = self.getUsuariosAtendidos().pop()
                    with open("Textos/UsuariosAtendidos.txt", "a") as archivo:
                        archivo.write(str(temp) + "\n")
                    sN1.push(temp)
                for i in range(sN1.size()):
                    temp2 = sN1.pop()
                    sN2.push(temp2)
                self.setUsuariosAtendidos(sN2)
                

usu1 = Usuario("Catalina", 1)
usu2 = Usuario("Andres", 2)
usu3 = Usuario("Mariana", 3)
usu4 = Usuario("Javier", 4)
usu5 = Usuario("Sofia", 5)
usus = [usu1, usu2, usu3, usu4, usu5]
T1 = TurnoUsuario()
for usuarios in usus:
    T1.registrar(usuarios)
#prueba a    
#T1.toFile()
#entre pruebas eliminar los txt :) uwu 7u7
#prueba b
T1.atenderSiguiente()
T1.atenderSiguiente()
T1.toFile()