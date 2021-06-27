import turtle
wn = turtle.Screen()
wn.bgcolor("darkgoldenrod")

noah = turtle.Turtle()
noah.shape("turtle")
noah.color("lightseagreen")
noah.pensize(5)
noah.speed(5)

for _ in range(3):          #to make equilateral triangle
    noah.forward(50)
    noah.left(120)

noah.penup()
noah.forward(100)

noah.pendown()

for _ in range(4):          #to make square
    noah.forward(50)
    noah.left(90)

noah.left(90)
noah.penup()
noah.forward(100)
noah.left(90)
noah.forward(200)
noah.left(90)
noah.forward(100)

noah.pendown()
for _ in range(6):          #to make hexagon
    noah.forward(50)
    noah.right(60)

noah.penup()
noah.forward(180)
noah.left(90)

noah.pendown()
for _ in range(8):          #to make octagon
    noah.forward(50)
    noah.left(45)