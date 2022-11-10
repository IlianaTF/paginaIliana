nombre=input ('escribe tu nombre')
if len(nombre) >=12:
    print('contra fuerte')
elif len(nombre)<12 and len(nombre)>6:
    print('contra media')
else:
    print('contra debil')