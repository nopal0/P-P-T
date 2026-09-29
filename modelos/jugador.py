class jugador:

    contador = 0 

    def __init__(self, nombre, id,creditos, puntos):

        self.nombre = nombre
        self.id = id
        self.creditos = creditos
        self.puntos = puntos
        self.vida = 100
        self.intentos = 5
        jugador.contador += 1

j1 = nopal = jugador("nopal", 100, 88, 850)
j2 = lapon = jugador("lapon", 100, 88, 500)

jugadores = [j1, j2]

for j in jugadores:

    print ("Tu nombre es: ", j.nombre)
    print ("Tienes un total de: ", j.puntos ,"puntos")

if jugador.contador <= 1:
    print("Existe un jugador", jugador.contador)
else:
    print("Existen", jugador.contador ,"jugadores")

PuntosNuevos = j1.puntos + j2.puntos
PuntosRestantes = j1.puntos - j2.puntos

print(j1.nombre ,"haz perdido", j2.puntos ,"Te quedan", PuntosRestantes ,"puntos")
print(j2.nombre ,"haz ganado", j2.puntos ,"puntos, tienes", PuntosNuevos)

j2.puntos = PuntosNuevos
j1.puntos = PuntosRestantes

