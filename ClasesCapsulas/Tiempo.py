class Tiempo:
    def __init__(self):
        self.__nombre=None
        self.__edad=None
        self.__pais=None
        self.__tiempo=None
        pass
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    @property
    def pais(self):
        return self.__pais
    
    @property
    def tiempo(self):
        return self.__tiempo
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @pais.setter
    def pais(self,pais):
        self.__pais=pais
    
    @edad.setter
    def edad(self,edad):
        self.__edad=edad

    @tiempo.setter
    def tiempo(self,tiempo):
        if(tiempo<0):
            print("El tiempo no puede ser negativo")
        else:
            self.__tiempo=tiempo    
    
    def calcularTiempo(self,ciclistas):
        
        print(ciclistas)

