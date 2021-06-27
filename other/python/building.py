import turtle

import turtle

rock = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("skyblue")
rock.color("slategray")
rock.shape("turtle")
rock.pensize(30)
rock.penup()

rock.goto(0, 350)
rock.pendown()
rock.forward(200)
rock.right(90)
rock.color("dimgray")
rock.forward(600)

wn.exitonclick()