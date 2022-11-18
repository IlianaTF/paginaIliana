import random 
puntos=0

for i in range(1,6):
    num1=random.randint(1,50)
    num2=random.randint(1,50)
    r=num1+num2
    print (num1, "+", num2,"= ")
    e1=int(input("tu respuesta es "))
    print()
    if e1==r:
        puntos=puntos+1
print("tuviste", score, "de 5")