import json

def leerDicc():
    with open("packs_compras.json", "r") as archivo:
        DP = json.load(archivo)
        return DP

def leerDiccJ():
    with open("jugadores.json", "r") as archivo:
        DP = json.load(archivo)
        return DP