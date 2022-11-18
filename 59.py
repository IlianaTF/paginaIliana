import random
colores=random.choice(["azul","verde","amarillo","rojo","naranja"])
print("escoge un color: azul, verde, amarillo, rojo o naranja")
otra= True
while otra==True:
    p=input("escribe el color seleccionado")
    p=p.lower()
    if colores==p:
        otra= False
    else:
        if colores=="azul":
            print("Sé que puedes eres grande como el mar AZUL")
        elif colores=="verde":
            print("sé que puedes no tienes que ponerte VERDE del desagrado")
        elif colores=="amarillo":
            print("sé que puedes eres igual de brillante que el sol AMARILLO")
        elif colores=="rojo":
            print("sé que puedes no tienes que ponerte ROJO del enojo")
        elif colores=="naranja":
            print("sé que puedes piensa como una NARANJA Einstein pensaría")