def ValidarQueSeaNumero(pregunta):

    i = 5

    while i > 0:
        try:

            d = int(input(pregunta))

            return d
        
        except ValueError:
            i -= 1
            print("Ingrese un numero entero")
            print("Le quedan ", i ," intentos")
            
            if i == 0:
                print("Sin intentos disponibles")
                return None

def ValidarQueSeaLetra(pregunta):

    i = 5

    while i > 0:
        try:

            d = str(input(pregunta))

            return d

        except ValueError:
            
            i -= 1
            print("Ingrese letras")
            print("Le quedan", i ,"intentos")

            if i == 0:

                print("Sin intentos posibles")
                return None