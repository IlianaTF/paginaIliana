comida={}
com1=input("ingrese una comida que te guste ")
comidas[1]=com1
com2=input("ingrese otra comida que te guste ")
comidas[2]=com2
com3=input("ingrese una tercera comida que te guste ")
comidas[3]=com3
com4=input("ingrese una ultima comida que te guste ")
comidas[4]=com4

print(comidas)
N=int(input("de cual de estas te quieres deshacer?"))
del comidas[N]
print(sorted(comidas.values()))