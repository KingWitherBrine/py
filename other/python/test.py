import turtle 
import random

wn = turtle.Screen()
wn.bgcolor("darkgoldenrod")

noah = turtle.Turtle()
noah.shape("turtle")
noah.color("lightseagreen")
noah.pensize(7)
noah.speed(10)
turtle.Screen().screensize(500, 500)

def draw_shape(n, r=20):
    for _ in range(n):
        noah.forward(r)
        noah.left(360 / n)

draw_shape(3) #to make equilateral triangle
    
noah.penup()
noah.forward(100)

noah.pendown()

noah.color("aquamarine")
draw_shape(4) #to make square
    
noah.left(90)
noah.penup()
noah.forward(100)
noah.left(90)
noah.forward(200)
noah.left(90)
noah.forward(100)

noah.color("dodgerblue")
noah.pendown()
draw_shape(6, 30) #to make hexagon

noah.penup()
noah.forward(180)
noah.left(90)

noah.color("chocolate")
noah.pendown()
draw_shape(8) #to make octagon

noah.penup()
noah.forward(150)

noah.color("red")
noah.pendown()
draw_shape(10) #to make a decagon
    
noah.penup()
noah.left(90)
noah.forward(300)
noah.left(90)
noah.forward(150)

noah.color("indianred")
noah.pendown() #to make a dodecagon
draw_shape(12, 30)

noah.penup()
noah.left(180)
noah.forward(150)
noah.pensize(5)

noah.color("lightseagreen")
noah.pendown()
for i in range(5): #to make a star
    noah.forward(110)
    noah.left(216)

noah.penup()
noah.right(180)
noah.forward(50)
noah.pendown()
noah.color("sandybrown")
draw_shape(14) #to make 14 sided shape

noah.penup()
noah.left(90)
noah.forward(200)
noah.color("seagreen")
noah.pendown()
draw_shape(16, 10)

noah.penup()
noah.left(90)
noah.forward(300)
noah.pendown()
draw_shape(18, 30)

noah.penup()
noah.right(180)
noah.forward(900)

noah.pendown()
noah.pensize(2)
noah.speed(0)
noah.hideturtle()


for i in range(50):
    noah.forward(i)
    noah.right(98)
    tings = ["green", "blueviolet", "lightcoral", "lightgoldenrodyellow", "skyblue", "violet", "forestgreen", "slateblue", "turquoise", "purple", "orange", "gold"]
    ting = random.randrange(len(tings))
    noah.pencolor(tings[ting])
noah.penup()
noah.forward(500)

noah.pencolor("lightblue")

noah.backward(900)
noah.left(100)
noah.forward(150)
noah.showturtle()
noah.pendown()
for i in range(50):
    noah.forward(40)
    noah.left(115)

    for i in range(50):
        noah.forward(40)
        noah.left(105)

        noah.right(115)
        for i in range(50):
            noah.forward(40)
            noah.left(105)

wn.exitonclick()