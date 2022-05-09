class Personaje:
    #Construtor
    def __init__(self,name,age):
        #Atributos
        #Un "_" es un dato protegido 
        self.__nombre=name
        self.__edad=age
        
        pass
    #Metodos get (Leer,administrar,obtener el valor de un atributo)
    #La analogia se toma como: Las palabras reservadas son un combo o promocion que ayuda a definir el metodo
    #"Property es para un getter "
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    #Metodos set (Enviar, ingresar , llevar un valor a un atributo )
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @edad.setter
    def edad(self,edad):
        if(edad<0):
            print("digite una edad valida")
        elif(edad>100):
            print("Por favor , ni yo llego a eso , respeto viejo ")
        else:
            self.__edad=edad

    
    
    

