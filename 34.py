print('1) cuadrado')
print('2) triangulo')
print()
seleccion=int(input('ingrese un numero'))
if seleccion==1:
    largo=int(input('ingrese el largo de un lado'))
    area=largo*largo
    print('el area del cuadrado es: ',area)
elif seleccion==2:
    altura=int(input('ingrese la altura de su traingulo'))
    base=int(input('ingrese la base del triangulo'))
    r=(base*altura)/2
    print ('el area del triangulo es: ',r)
else:
    print('error')