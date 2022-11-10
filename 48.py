inte=0
vuelta='si'
while vuelta=='si':
    nombre=input('ingrese el nombre de la persona invitada')
    print(nombre, 'esta invitado a su fiesta')
    inte=inte+1
    vuelta=input('quiere invitar a alguien mas? (si/no)')
print('usted tiene ', inte, 'personas invitadas a su fiesta')
