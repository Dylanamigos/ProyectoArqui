import Baraja as bar

StackCartas = bar.BarajearCartas(10) #Crea un Stack de Cartas barajeadas con 10 paquetes de cartas.
CartasJugador = []
CartasCrupier = []


def VerCartas(BarajaAVer):
    for i in BarajaAVer:
        print(str(i.number) + i.pila) #Funcion que imprime las cartas en la consola.
    return

def Inicio(): #Logica de Inicio de cada ronda
    if (len(StackCartas) != 0):
        CartasJugador.append(StackCartas.pop())
        CartasCrupier.append(StackCartas.pop())
        CartasJugador.append(StackCartas.pop())
        CartasCrupier.append(StackCartas.pop())
        YourTurn()
        return
    else:
        return ("Error en el Inicio de cada Ronda de Blackjack")


def YourTurn(): #Logica de el turno del jugador
    VerCartas(CartasJugador)
    PosibilidadesBlackjack()
    

def CrupierTurn(): #Logica del turno del crupier.
    return

def PosibilidadesBlackjack(): #Distintas Posibilidades, Dividir, Doblar, Pedir, Pararse
    
    return

Inicio()

