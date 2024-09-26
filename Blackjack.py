import Baraja as bar

StackCartas = bar.BarajearCartas(6) #Lista de cartas en la pila
CartasJugador = [] #Cartas del jugador se resetea cada ronda
CartasCrupier = [] #Cartas Crupier se resetea cada ronda

def CrearStack():
    global StackCartas #Llamar a StackCartas global
    StackCartas = bar.BarajearCartas(6)

def VerCartas(BarajaAVer):
    for i in BarajaAVer:
        print((i.number) + " " + i.pila) #Funcion que imprime las cartas en la consola.
    return

def Inicio(): #Logica de Inicio de cada ronda
    print(len(StackCartas))
    CartasCrupier.clear()
    CartasJugador.clear()
    if (len(StackCartas) > 260): #Aproximadamente la mitad
        CartasJugador.append(StackCartas.pop())
        CartasCrupier.append(StackCartas.pop())
        CartasJugador.append(StackCartas.pop())
        CartasCrupier.append(StackCartas.pop())
        YourTurn()
        return
    else:
        StackCartas.clear() #Eliminamos todo
        CrearStack() #Volvemos a shufflear
        Inicio() #Llamamos a Inicio de Blackjack de nuevo.
        return


def YourTurn(): #Logica de el turno del jugador
    print(" ") #Salto de Linea
    VerCartas(CartasJugador) 
    SumaJugador = 0
    for i in CartasJugador:
        SumaJugador += CartaToInt(i.number)
    print ("Suma del Jugador: " + str(SumaJugador)) #Muestra Cartas Jugador
    print ("Carta del Crupier: " + str(str(CartasCrupier[0].number) + " " + str(CartasCrupier[0].pila))) #Muestra Cartas Crupier
    if (SumaJugador <= 21):
        PosibilidadesBlackjack(SumaJugador)
    else:
        print("Busted ")
        Inicio()
        return

def CrupierTurn(SumaJgdr): #Logica del turno del crupier.
    print(" ")
    VerCartas(CartasCrupier)
    SumaCrupier = 0
    for i in CartasCrupier:
        SumaCrupier += CartaToInt(i.number)
    print("Suma del Jugador es: " + str(SumaJgdr))
    print("Suma del Crupier es: " + str(SumaCrupier))
    if(SumaCrupier > 21):
        print("Crupier Busted ")
        return "Ganaste"
    elif(SumaCrupier <= 17):
        CartasCrupier.append(StackCartas.pop())
        CrupierTurn(SumaJgdr)
    else:
        if (SumaJgdr > SumaCrupier):
            print("Ganaste")
        elif (SumaJgdr < SumaCrupier):
            print("Perdiste")
        else:
            print("Empate")
    CartasCrupier.clear()
    CartasJugador.clear()
    Inicio()
    return

def PosibilidadesBlackjack(SumaJgdr): #Distintas Posibilidades, Dividir, Doblar, Pedir, Pararse
    intencion = int(input("Ingrese tu intencion: ")) #1) Pedir, 2) Parar, 3) Doblar, 4) Dividir
    dicc = {
        "Pedir": 1,
        "Parar": 2,
        "Doblar": 3,
        "Dividir": 4,
    }
    if(intencion == dicc["Pedir"]):
        CartasJugador.append(StackCartas.pop())
        YourTurn()
        return
    elif(intencion == dicc["Parar"]): #Luego codeo Doblar y Dividir xd
        CrupierTurn(SumaJgdr)
        return
    return

def CartaToInt(number):
    try:
        int(number)
        return int(number)
    except ValueError:
        if (number == "A"):
            return int(1)
        elif (number == "J"):
            return int(10)
        elif (number == "Q"):
            return int(10)
        elif (number == "K"):
            return int(10)
    return

Inicio()

