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

    def __init__(self, nombre, id,creditos, puntos):

        self.nombre = nombre
        self.id = id
        self.creditos = creditos
        self.puntos = puntos
        self.vida = 100
        self.intentos = 5
        jugador.contador += 1


j1 = nopal = jugador("nopal", 100, 88, 10)
j2 = lapon = jugador("lapon", 100, 88, 10)
j3 = lugia = jugador("lugia", 100, 88, 10)

j1.PerderPuntos(5)
j2.ComprobarYRestar()
j3.PerderPuntos(15)

jugadores    = [j1, j2, j3]

prueba = j1.ObtenerPuntos()

for j in jugadores:
    j.MostrarDatos()

print(prueba)