import math
radio=int(input('cual es el radio del cilindro'))
prof=int(input('cual es la profundidad del cilindro'))
area=math.pi*(radio**2)
volumen=area*prof
print(round(volumen,3))