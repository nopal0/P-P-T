from utilidades.UtilidadesDicc import leerDicc
from utilidades.validaciones import ValidarQueSeaNumero
from modelos.jugador import jugador

def MostrarPaquetes():

    PC = leerDicc()

    for nombre , paquete in PC.items():
        print (nombre)
        print ("El precio de este paquete es de:", paquete["Puntos"])
        print ("Y tiene un valor de: ", paquete["Creditos"])

def v():
    try:
        PuntosAPagar = int(input("Ingrese el precio del paquete que dese: "))
    except ValueError:
        
        print ("")



def MainMenuCompras():

    MostrarPaquetes()

    PuntosAPagar = ValidarQueSeaNumero("Ingrese el precio de paquete que deses")

    Valor = jugador.ObtenerCreditos(PuntosAPagar)
    print (Valor)