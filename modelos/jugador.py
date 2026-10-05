from utilidades.menus import leerDicc , leerDiccJ

PC = leerDicc()

class jugador():

    contador = 0
    PuntosPerdidos = 10

    def PerderPuntos(self, PuntosPerdidos):
        if PuntosPerdidos <= 0:
             raise ValueError ("No puedes ingreasar puntos negativo")
        else:
            if self._puntos >= PuntosPerdidos:    
                self._puntos -= PuntosPerdidos
                print("Has perdido", PuntosPerdidos ,"tus nuevos puntos son", self._puntos , self.nombre)
            else:
                print("Sin puntos suficientes", self.nombre)

    def ComprobarYRestar(self):
            self.PerderPuntos(jugador.PuntosPerdidos)

    def MostrarDatos(self):
         print("Hola", self.nombre)
         print("Tus puntos son", self._puntos)
         print("Tus creditos son", self._creditos)

    def ObtenerPuntos(self):
        return self._puntos

    def ComprobarPuntosCompra(self, PuntosAPagar):
        if PuntosAPagar <= self._puntos:
            return True
        else:
            return False

    def CambiarPuntos(self, NuevosPuntos):
        if NuevosPuntos < 0:
            raise ValueError("Los puntos no pueden ser negativos", self.nombre)
        else:
              self._puntos = NuevosPuntos
              print ("Tus nuevos puntos son", self._puntos)
              return self.ObtenerPuntos()

    def SumarCRestarP(self, PuntosAPagar , CreditosComprados):
        if self._puntos >= PuntosAPagar:
            if CreditosComprados <= 51:
                self._creditos += CreditosComprados
                self._puntos -= PuntosAPagar
                print ("Tus nuevos puntos son", self._puntos)
                print ("Tus nuevos creditos son", self._creditos)
            else:
                print ("Ese paquetede creditos no existe")

        else:
            print("Puntos insuficientes")
        
    def ComprarCreditos(self , PuntosAPagar):

        Valor = PC

        for paquete in PC.values():
            if paquete["Puntos"] == PuntosAPagar:
                CreditosComprados = paquete["Creditos"]
                break

        if self._puntos >= 10:

            if PuntosAPagar >= paquete["Puntos"]:
                self._creditos + paquete["Creditos"]
                self.SumarCRestarP(PuntosAPagar , CreditosComprados)

            elif PuntosAPagar == 25:

                if self.ComprobarPuntosCompra(PuntosAPagar) == True:

                    CreditosComprados = 80
                    self.SumarCRestarP(PuntosAPagar , CreditosComprados)

                else:
                    print ("Puntos insuficientes")
                
            elif PuntosAPagar == 50:

                if self.ComprobarPuntosCompra(PuntosAPagar) == True:

                    CreditosComprados = 150
                    self.SumarCRestarP(PuntosAPagar , CreditosComprados)

                else:
                    print("Puntos insuficientes")

            else:
                 print ("Opcion invalida")
                 print ("Ingrese una de las siguientes opciones")
                 print ("10 , 25 , 50")

        else:
             print("Puntos insuficientes")

    def GuardarDatosNuevoJugador(self, n, c, p, cc):
        try:
            DJ = leerDiccJ()
        except FileNotFoundError:
            DJ = {}

        DJ[id]={
            "nombre":n,
            "creditos": c,
            "puntos": p,
            "contrasena": cc,
        }

    def CrearId(self):
        id = 238 * jugador.contador * 4
        return id

    def __init__(self, nombre, idi,creditos = 100, puntos= 100):

        if nombre.strip() == "":
             raise ValueError ("Tienes que ingresar un nombre")
        else:
            self.nombre = nombre.strip()

        if  idi == float(idi):
            self.id = idi
        else:
             raise ValueError(".l.")

        if creditos >= 0:
            self._creditos = creditos
        else:
             raise ValueError ("No puedes ingresar creditos negativos")

        if puntos >= 0:
            self._puntos = puntos
        else:
            raise ValueError ("No puedes ingresar puntos negativos")
        
        self.vida = 100
        self.intentos = 5
        jugador.contador += 1