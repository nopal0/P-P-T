from interfaz.menu_compra import MainMenuCompras

class jugador():

    contador = 0
    PPerdidos = 10

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

    def CrearId(self):
        id = 238 * jugador.contador * 4
        return id

    def ObtenerPuntos(self):
        return self._puntos

    def RestarPuntos(self, PuntosPerdidos):
        try:
            if PuntosPerdidos != int:
                if self._puntos >= PuntosPerdidos:
                    NuevosPuntos = self._puntos - PuntosPerdidos
                    
                    return NuevosPuntos

                else:

                    return False
        except ValueError:
            pass
        
    def CambiarPuntos(self, NuevosPuntos):

        if NuevosPuntos < 0:
            raise ValueError("Los puntos no pueden ser negativos", self.nombre)
        
        else:
              self._puntos = NuevosPuntos
              print ("Tus nuevos puntos son", self._puntos)
              return self.ObtenerPuntos()

    def PerderPuntos(self, PuntosAPagar):
        
        if PuntosAPagar <= 0:
             
             raise ValueError ("No puedes ingreasar puntos negativo")
        
        else:
        
            if self._puntos >= PuntosAPagar:    
        
                self._puntos -= PuntosAPagar

                return self.ObtenerPuntos
        
            else:

                return False

    def ComprobarYRestar(self):
        
            self.PerderPuntos(jugador.PuntosPerdidos)
            
    def ComprobarPuntosCompra(self, PuntosAPagar):
        
        if self._puntos >= PuntosAPagar:
            return True
        
        else:
            return False

    def SumarCRestarP(self, PuntosAPagar , CreditosComprados):

        if self._puntos >= PuntosAPagar:
            
            if CreditosComprados <= 50:

                self._creditos += CreditosComprados
                self._puntos -= PuntosAPagar
                print ("Tus nuevos puntos son", self._puntos)
                print ("Tus nuevos creditos son", self._creditos)

            else:
                print ("Ese paquetede creditos no existe")

        else:
            print("Puntos insuficientes")

    def xd():
        MainMenuCompras()
