#again=input('quieres iniciar el juego?')

#while again=='si':
    #print('estas dentro del loop')
    #again=input('presiona si para continuar y no para salir')
#print('loop terminado')

total=0
interacion=0
while total<100:
    num=int(input('ingrese un numero'))
    total=total+num
    interacion=interacion+1
    print ('repeticion: ',interacion, 'el total es ', total)
    print ('*'*10)