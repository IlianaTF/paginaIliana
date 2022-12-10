import turtle
import random 

lineas=random.randint(5,20)

for i in range (0,lineas):
    longitud=random.randint(25,100)
    giro=random.randint(1,365)
    turtle.forward(longitud)
    turtle.right(giro)

turtle.exitonclick()