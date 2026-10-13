import json
from pathlib import Path

def leerDiccJ():
    ruta = Path(__file__).resolve().parent.parent / "datos" / "jugadores.json"
    with open(ruta, "r") as archivo:
        DP = json.load(archivo)
        return DP
