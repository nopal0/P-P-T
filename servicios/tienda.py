from persistencia.catalogo_json import leerDicc

PC = leerDicc()

def ObtenerCreditos(PuntosAPagar):

    for puntos in PC.values():
        if PuntosAPagar == puntos["Puntos"]:
            return puntos["Creditos"]
    else:
        return False

def ComprarCreditos(Jugador, PuntosAPagar):

    if Jugador.ComprobarPuntosCompra(PuntosAPagar) == True:
        
        p = Jugador.ComprobarYRestar()

