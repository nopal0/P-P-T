PacksCompras ={
    "Paquete1" :{ 
        "Puntos" : 10,
        "Creditos" : 25
},
    "Paquete2" : {
        "Puntos" : 25,
        "Creditos" : 80
},}
puntos = 10
creditos = 50
if PacksCompras["Paquete1"]["Puntos"] >= puntos:
    NuevosCreditos = PacksCompras["Paquete1"]["Creditos"] + creditos
    NuevosPuntos = puntos -  PacksCompras["Paquete1"]["Puntos"]
else:
    print("bobo")

print (NuevosPuntos)
print (NuevosCreditos)