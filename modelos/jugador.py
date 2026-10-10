from utilidades.UtilidadesDicc import leerDicc

PC = leerDicc()

class jugador():

    contador = 0
    PuntosPerdidos = 10

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

    def MostrarDatos(self):
         print("Hola", self.nombre)
         print("Tus puntos son", self._puntos)
         print("Tus creditos son", self._creditos)

    def ObtenerPuntos(self):
        return self._puntos

    def CambiarPuntos(self, NuevosPuntos):
        if NuevosPuntos < 0:
            raise ValueError("Los puntos no pueden ser negativos", self.nombre)
        else:
              self._puntos = NuevosPuntos
              print ("Tus nuevos puntos son", self._puntos)
              return self.ObtenerPuntos()

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
            
    def ComprobarPuntosCompra(self, PuntosAPagar):
        
        if PuntosAPagar >= self._puntos:
            return False
        
        else:
            return True

    def ComprarCreditos(self , PuntosAPagar):

        if PuntosAPagar == PC["Paquete1"]["Puntos"]:
            Precio = PC["Paquete1"]["Puntos"]
            Valor = PC["Paquete1"]["Creditos"]

        if self._puntos >= 10:

            if PuntosAPagar >= Precio:
                self.SumarCRestarP(PuntosAPagar , Valor)

            else:
                 print ("Opcion invalida")
                 print ("Ingrese una de las siguientes opciones")
                 print ("10 , 25 , 50")

        else:
             print("Puntos insuficientes")

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
        