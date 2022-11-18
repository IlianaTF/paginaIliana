import random
r=random.randint(1,10)
correcto==false 
while correcto==falso:
    user=int(input('adivina el numero entre el 1-10 tienes oportunidades infinitas'))
    if user==r:
        correcto==true
    elif user>r:
        print("muy alto")
    else:
        print ("muy bajo")
