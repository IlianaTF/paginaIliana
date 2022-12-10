import turtle
turtle.shape("turtle") 

turtle.begin_fill() 
for i in range (0,4):
    turtle.forward(50)
    turtle.left(90)
    turtle.color("black","red") 
turtle.penup() 
turtle.end_fill() 

turtle.forward(100)

turtle.begin_fill() 
for i in range (0,4):
    turtle.forward(50)
    turtle.left(90)
    turtle.color("black","blue") 
turtle.penup() 
turtle.end_fill() 

turtle.forward(100)

turtle.begin_fill() 
for i in range (0,4):
    turtle.forward(50)
    turtle.left(90)
    turtle.color("black","green") 
turtle.end_fill() 




turtle.exitonclick()