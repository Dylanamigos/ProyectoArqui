import random as rd #Para barajear las cartas xD

class Carta:
    def __init__(self, number, pila):
        self.number = number
        self.pila = pila
#Clase carta con numero de valor y de que pinta es 

def CrearBaraja():
    Baraja = []
    for i in range(10):
        Baraja.append(Carta(i+1, "Corazones"))
        Baraja.append(Carta(i+1, "Diamantes"))
        Baraja.append(Carta(i+1, "Treboles"))
        Baraja.append(Carta(i+1, "Picas"))
    for i in range(3):
        Baraja.append(Carta(10, "Corazones"))
        Baraja.append(Carta(10, "Diamantes"))
        Baraja.append(Carta(10, "Picas"))
        Baraja.append(Carta(10, "Treboles"))
    return Baraja
#Crea una Baraja con 52 cartas

#n es el numero de paquetes de cartas a barajear, no se juega con un solo paquete
def BarajearCartas(n):
    StackCartas = []
    for i in range (n):
        StackCartas.extend(CrearBaraja())
    rd.seed(37) #Mi numero favorito xd
    rd.shuffle(StackCartas)
    return StackCartas #Este seria el Stack de Cartas
    


    
