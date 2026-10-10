from utilidades.validaciones import ValidarQueSeaNumero

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
    i = 5
    while i > 0:

        try:
            r = int(input("Que opcion eligiras: "))
            return r
        
        except ValueError:

            i -= 1
            print("Ingrese un numero")
            print("Intente nuevamente")
            
            if i == 0:
            
                print("Sin intentos posibles")
                return None