import turtle 

seurat = turtle.Turtle()


dot_distance = 25
width = 5
height = 7

seurat.penup()

for y in range(height):
    for i in range(width):
        seurat.dot()
        seurat.forward(dot_distance)
    seurat.backward(dot_distance * width)
    seurat.right(90)
    seurat.forward(dot_distance)
    seurat.left(90)

painter = turtle.Turtle()

painter.pencolor("blue")
for i in range(50):
    painter.forward(50)
    painter.left(123) # Let's go counterclockwise this time 
    
painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)
    
painter.pencolor("green")
for i in range(50):
    painter.forward(150)
    painter.left(123)

painter.pencolor("grey")
for i in range(50):
    painter.forward(200)
    painter.left(123)    
    
turtle.done()
