import json
class jugador:
    def __init__(self, nombre, vida,creditos):
        self.nombre = nombre
        self.vida = vida
        self.creditos = creditos

nopal = jugador("nopal", 100, 88)
lapon = jugador("lapon", 100, 88)


def main():
    print(nopal.nombre)

main()