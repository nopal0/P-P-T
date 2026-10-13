from interfaz.entradas import ValidarQueSeaNumero

def MainMenuPrincipal():

    MostrarOpcionesPrincipales()
    R1 = ValidarQueSeaNumero("Que opcion eligiras: ")

    if R1 is not None:
        print ("")
        return R1
    else:
        print("")
        return None

def MostrarOpcionesPrincipales():

    OpcionesPrincipales = ["[1]Jugar\n[2]Amigos\n[3]Comprar creditos\n[4]Mostrar datos"]

    for O in OpcionesPrincipales:
        print(O)

def MenuPrincipalRespuesta():
    r = ValidarQueSeaNumero("Que opcion eligiras: ")
    return r

def MostrarDatos(Jugador):
     print("Hola", Jugador.nombre)
     print("Tus puntos son", Jugador._puntos)
     print("Tus creditos son", Jugador._creditos)
