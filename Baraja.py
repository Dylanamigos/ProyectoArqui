import random as rd #Para barajear las cartas xD

class Carta:
    def __init__(self, number, pila):
        self.number = number
        self.pila = pila
#Clase carta con numero de valor y de que pinta es 

def CrearBaraja():
    Baraja = []
    for i in range(9):
        Baraja.append(Carta(str(i+2), "Corazones"))
        Baraja.append(Carta(str(i+2), "Diamantes"))
        Baraja.append(Carta(str(i+2), "Treboles"))
        Baraja.append(Carta(str(i+2), "Picas"))
    Baraja.append(Carta("J", "Corazones"))
    Baraja.append(Carta("J", "Diamantes"))
    Baraja.append(Carta("J", "Picas"))
    Baraja.append(Carta("J", "Treboles"))
    Baraja.append(Carta("K", "Corazones"))
    Baraja.append(Carta("K", "Diamantes"))
    Baraja.append(Carta("K", "Picas"))
    Baraja.append(Carta("K", "Treboles"))
    Baraja.append(Carta("Q", "Corazones"))
    Baraja.append(Carta("Q", "Diamantes"))
    Baraja.append(Carta("Q", "Picas"))
    Baraja.append(Carta("Q", "Treboles"))
    Baraja.append(Carta("A", "Corazones"))
    Baraja.append(Carta("A", "Diamantes"))
    Baraja.append(Carta("A", "Picas"))
    Baraja.append(Carta("A", "Treboles"))
    return Baraja
#Crea una Baraja con 52 cartas

#n es el numero de paquetes de cartas a barajear, no se juega con un solo paquete
def BarajearCartas(n):
    StackCartas = []
    for i in range (n):
        StackCartas.extend(CrearBaraja())
    rd.seed(rd.randint(0, 37)) #Mi numero favorito xd
    rd.shuffle(StackCartas)
    return StackCartas #Este seria el Stack de Cartas
    


    
