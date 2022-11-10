a=50
adivi=int(input('adivina en que numero estoy pensando'))
contador=1
while adivi !=a:
    if adivi< a:
        print('muy bajo')
    else:
        print('muy alto')
    contador=contador+1
    adivi=int(input('sigue adivinando'))
print('muy bien hecho, tuviste', contador,'intentos')