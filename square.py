import turtle
window = turtle.Screen()
bgcolor = turtle.bgcolor("navy")
pen = turtle.Turtle()
pencolor = pen.pencolor("white")


for i in range(4):
    pen.down()
    pen.forward(200)
    pen.left(90)

turtle.done()