from persistencia.catalogo_json import leerDicc
from interfaz.entradas import ValidarQueSeaNumero
from servicios.tienda import ObtenerCreditos
from modelos.jugador import jugador

def MostrarPaquetes():

    PC = leerDicc()

    for nombre , paquete in PC.items():
        print (nombre)
        print ("El precio de este paquete es de:", paquete["Puntos"])
        print ("Y tiene un valor de: ", paquete["Creditos"])

def MainMenuCompras():

    MostrarPaquetes()

    PuntosAPagar = ValidarQueSeaNumero("Ingrese el precio de paquete que deses")

    ObtenerCreditos(PuntosAPagar)
    print (jugador._puntos)
