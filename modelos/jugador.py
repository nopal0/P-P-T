class jugador():

    contador = 0
    PuntosPerdidos = 10

    def PerderPuntos(self, PuntosPerdidos):
        if self.puntos >= PuntosPerdidos:    
            self.puntos -= PuntosPerdidos
            print("Has perdido", PuntosPerdidos ,"tus nuevos puntos son", self.puntos , self.nombre)
        else:
                print("Sin puntos suficientes", self.nombre)

    def ComprobarYRestar(self):
            self.PerderPuntos(jugador.PuntosPerdidos)

    def MostrarDatos(self):
         print("Hola", self.nombre)
         print("Tus puntos son", self.puntos)
         print("Tus creditos son", self.creditos)

    def ObtenerPuntos(self):
         return self.puntos

    def __init__(self, nombre, id,creditos = 100, puntos= 100):

        if nombre.strip() == "":
             raise ValueError ("Tienes que ingresar un nombre")
        else:
            self.nombre = nombre.strip()

        self.id = id

        if creditos >= 0:
            self.creditos = creditos
        else:
             raise ValueError ("No puedes ingresar creditos negativos")

        if puntos >= 0:
            self.puntos = puntos
        else:
            raise ValueError ("No puedes ingresar puntos negativos")
            
        
        self.vida = 100
        self.intentos = 5
        jugador.contador += 1



j1 = nopal = jugador("nopal", 100, 88, 10)
j2 = megalodon = jugador(" Megalodon ", 48484879 , puntos= 25)
j1.puntos = -50
j1.ObtenerPuntos()

jugadores    = [j1, j2]

for j in jugadores:
    j.MostrarDatos()

try:
    j2 = lapon = jugador(" lapon ", 100, -88, 0)
except ValueError:
    print("No se puede crear un jugador con creditos negativos")
try:
    j3 = lugia = jugador("  ", 100, 88, 0)
except ValueError:
     print("No se puede crear un jugador sin nombre")

try:
     j4 = lugia = jugador("lugia", 100, 2 , -38)
except ValueError:
     print("No se puede crear un jugador con puntos negativos")


