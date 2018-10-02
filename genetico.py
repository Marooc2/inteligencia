import numpy
import random

def Parejas(Poblacion):
    Aleatorio = random.sample(range(int(Poblacion/2),Poblacion),int(Poblacion/2))
    Pareja = {}
    for i in range(int(Poblacion/2)):
        Pareja[i],Pareja[Aleatorio[i]] = Aleatorio[i],i
    return Pareja

def Inicializacion(Poblacion):
    global Individuos
    global Mejor
    Individuos = {}
    for i in range(Poblacion):
        Individuos[i] = numpy.random.choice(range(1,8),8,replace=True)
    print('---Inicializacion----')
    Mostrar(Poblacion)
	
def Seleccion(Poblacion): #torneo
    print('---Seleccion----')
    Pareja = Parejas(Poblacion)
    print('Parejas',Pareja)
    for k,v in Pareja.items():
        if Idoneidad(Individuos[k]) >= Idoneidad(Individuos[v]):
            Individuos[v] = Individuos[k]
    Mostrar(Poblacion)
            
def Idoneidad(Tablero):
    Atacadas = 0
    for i in range(len(Tablero)):
        for j in range(i + 1,len(Tablero)):
            if Tablero[i] == Tablero[j]:
                Atacadas += 1
            Dif = j - i
            if Tablero[i] == Tablero[j] - Dif or Tablero[i] == Tablero[j] + Dif:
                Atacadas += 1
    return 28-Atacadas

def Cruce(Poblacion):
    print('-----Cruce ------')
    Pareja = Parejas(Poblacion)
    print('Parejas',Pareja)
    item = 0
    for k,v in Pareja.items():
        if item % 2 == 0:
            Punto = random.randint(1,7)
            print('punto',Punto)
            Hijo1 = []
            Hijo2 = []
            Padre1 = Individuos[k]
            Padre2 = Individuos[v]
            Hijo1.extend(Padre1[0:Punto])
            Hijo1.extend(Padre2[Punto:])
            Hijo2.extend(Padre2[0:Punto])
            Hijo2.extend(Padre1[Punto:])
            Individuos[k] = Hijo1
            Individuos[v] = Hijo2
        item = item+1
    Mostrar(Poblacion)
def Mutacion(Poblacion):
    print('-----Mutacion ----')
    for i in range(int(Poblacion/2)):
        ElegirI = random.randint(0,Poblacion-1)
        print(ElegirI)
        ElegirPos = random.randint(0,7)
        print(ElegirPos)
        ElegirGen = random.randint(1,8)
        print(ElegirGen)
        Individuos[ElegirI][ElegirPos] = ElegirGen
        print("****")
    Mostrar(Poblacion)

def Mostrar(Poblacion):
    for i in range(Poblacion):
        print(Individuos[i],'f(x)=',Idoneidad(Individuos[i]))

Poblacion = 8
Inicializacion(Poblacion)
Seleccion(Poblacion)
Cruce(Poblacion)
Mutacion(Poblacion)
