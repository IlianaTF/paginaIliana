num1=int(input('ingrese un numero'))
total=num1
again='si'
while again=='si':
    num2=int(input('ingrese otro numero'))
    total=total+num2
    again=input('quiere ingresar otro numero? (si/no)')
print('el total es: ', total)