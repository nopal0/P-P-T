import json
from pathlib import Path

def leerDicc():
    ruta = Path(__file__).resolve().parent.parent / "config" / "packs_compras.json"
    with open(ruta, "r") as archivo:
        DP = json.load(archivo)
        return DP
