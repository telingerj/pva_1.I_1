import turtle

# rovnostranný trolúhelník

"""

zelva = turtle.Turtle()

for i in range(3):
    zelva.forward(100)
    zelva.left(120)


turtle.done()

"""

zelva = turtle.Turtle()

turtle.width(5)

n = 100
for i in range(n):
    if i % 2 == 0:
        turtle.pencolor("red")
    else:
        turtle.pencolor("blue")
    turtle.forward(1000 / n)
    turtle.left(360 / n)


turtle.done()