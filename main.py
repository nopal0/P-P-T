from modelos.jugador import jugador

j1 = nopal = jugador("nopal", 100, 88, 10)
j2 = megalodon = jugador(" Megalodon ", 48484879)
j4 = lugia = jugador("lugia", 100, 2 , 38)

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
     j4.PerderPuntos(-388)
except ValueError:
     print("No se puede tener puntos negativos")

try:
     j5 = l = jugador("Lonche", "12212")
except ValueError:
     print("!!! Error en id, ingresar numeros !!!")

j2.CambiarPuntos(0)
j2.CambiarPuntos(80)

try:
     j2.CambiarPuntos(-100)
except ValueError:
     print("!!! No numeros negativos !!!")

PuntosActuales = j2.ObtenerPuntos()     
print (PuntosActuales)

j1.ComprarCreditos(10)
j2.SumarCRestarP(10,150)
j4.SumarCRestarP(80 , 150)

n = input("Cual es tu nombre: ")

id = 485

j100 = jugador(n, id)

j100.MostrarDatos()