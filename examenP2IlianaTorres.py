import math 

r=(input('quieres iniciar a calcular?'))

while r=='si' or r=='Si':
    a=int(input('ingrese el valor de a'))
    b=int(input('ingrese el valor de b'))
    c=int(input('ingrese el valor de c'))
    r1=b**2
    a2=4*a
    a3=a2*c
    a4=r1-a3
    if a4==0:
        print('Discriminante negativo, hay raíces imaginarias')
    else:
        r1=b**2
        a2=4*a
        a3=a2*c
        a4=r1-a3
        raiz= math.sqrt(a4) 
        r2=-b+raiz
        r4=-b-raiz
        r3=2*a
        final1=r2//r3
        final2=r4//r3
    print('x1= ',final1, "x2= ",final2)
    print('La ecuación factorizada es (x-',final1,')' ,'* (x-',final2,')')
    r=input('quieres seguir calculando si/no?')
print('gracias por calcular')
    
