import math 
a=input('''
Elige lo que quieras calcular
co)CONO
ci)CILINDRO
''')
a=a.lower()
if a=='co':
    h=int(input('ingrese la altura del cono'))
    r=int(input('ingrese el radio del cono'))
    a1=r**2
    a4=a1*h
    a2=math.pi*a4
    a3=a2/3
    print('el volumen del cono es: ',(round(a3,2)))
elif a=='ci':
    h=int(input('ingrese la altura del cilindro'))
    r=int(input('ingrese el radio del cilindro'))
    a1=r**2
    a2=math.pi*a1
    print('el volumen del cono es: ',(round(a2,2)))
else:
    print('Dulce o truco')

