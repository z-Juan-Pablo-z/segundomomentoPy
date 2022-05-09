#importar las clases
import imp
from ClasesCapsulas.Personajes import Personaje
from ClasesCapsulas.Tiempo import Tiempo
#Creando objetos
# personaje=Personaje("juan",800)
# personaje.nombre="Pablo"
# personaje.edad=18



# print(personaje.nombre)
# print(personaje.edad)




ciclistas=[]

opcion = 1
while(opcion!=0):
    ciclista =Tiempo()
    print("Digitar 1 para registrar un nuevo ciclista")
    print("Digitar 2 para recibir {nombre,edad,pais,tiempo} del mejor tiempo registrado ")
    print(" Digitar 0 para SALIR ")
    opcion=int(input("Digita una opcion "))
    if(opcion==0):
        break
    elif(opcion==1):
        ciclista.nombre=input(" Digite el nombre del ciclista ")
        ciclista.edad=int(input(" Digite la edad del ciclista "))
        ciclista.pais=input(" DIgite el pais del ciclista ")
        ciclista.tiempo = int(input(" Digite el tiempo logrado por el ciclista "))
        ciclistas.append(ciclista)
    elif(opcion==2):
        tiempoMenor=ciclistas[0].tiempo
        for ciclistaGanador in ciclistas:
            if(ciclistaGanador.tiempo<tiempoMenor):
                tiempoMenor=ciclistaGanador.tiempo
        print(f"el ciclista con el tiempo menor logrado  {ciclistaGanador.tiempo}")
        print(f"Los datos del ciclista son : {ciclistaGanador.nombre} su edad es : {ciclistaGanador.edad} el pais perteneciente {ciclistaGanador.pais} y el maravilloso tiempo logrado {ciclistaGanador.tiempo}")
    else:
        print("Digite por favor una opcion valida")

    