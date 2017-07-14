import turtle 

painter = turtle.Turtle()
painter.pensize(3)
painter.speed(0)

painter.pencolor("blue")
for i in range(120):
    painter.forward(350)
    painter.left(111) # Let's go counterclockwise this time 
    
painter.pencolor("red")
for i in range(120):
    painter.forward(270)
    painter.left(111)
    
painter.pencolor("green")
for i in range(120):
    painter.forward(230)
    painter.left(111)

painter.pencolor("black")
for i in range(119):
    painter.forward(200)
    painter.left(137)
    
turtle.done()
