# Los metodos Lab* recibian self; ahora reciben el mismo jugador como argumento.

def LabComprobarPuntosNoSeanNegativosGeneral(Jugador):

    if Jugador._puntos > 0:
        return True

    else:
        return False

def LabRestarYComprobarPuntos(Jugador, PuntosPerdidos):

    if LabComprobarPuntosNoSeanNegativosGeneral(Jugador) == True:
        NP = Jugador._puntos - PuntosPerdidos
        return NP

    else:
        return False

def LabSumarYComprobarPuntos(Jugador):
    if LabComprobarPuntosNoSeanNegativosGeneral(Jugador) == True:
        print

def LabCreditosComprobarPositivoGeneral(Jugador):

    if Jugador._creditos > 0:
        return True

    else:
        return False

def LabRestatYComprobarCreditos(Jugador, CreditosPerdidos):

    if LabCreditosComprobarPositivoGeneral(Jugador) == True:
        NC = Jugador._creditos - CreditosPerdidos
