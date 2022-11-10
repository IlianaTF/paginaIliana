palabra=input('ingrese una palabra')
prim=palabra [0]
largo=len(palabra)
r=palabra [1:largo]
if prim != 'a' and prim !='e' and prim !='i' and prim !='o' and prim !='u':
    palabranuev= r + prim + 'ay'
else:
    palabranuev=palabra + 'way'
print(palabranuev.lower())