import turtle
tortuguita = turtle.Turtle()
fondo=turtle.Screen()
fondo.bgcolor('beige')

#J
tortuguita.pencolor("green")
tortuguita.pensize(28)
tortuguita.shape("circle")
tortuguita.forward(80)
tortuguita.left(90)
tortuguita.forward(135)
tortuguita.left(90)
tortuguita.forward(70)
tortuguita.right(180)
tortuguita.forward(140)
tortuguita.right(70)
tortuguita.penup()
tortuguita.goto(0, 0)
tortuguita.pendown()
tortuguita.goto(105, 0)
a=tortuguita.pos()
#A
tortuguita.goto(a)
tortuguita.right(290)
tortuguita.pencolor("purple")
tortuguita.pensize(28)
tortuguita.shape("circle")
tortuguita.left(70)
tortuguita.forward(130)
tortuguita.right(130)
tortuguita.forward(100)
tortuguita.right(120)
tortuguita.forward(50)
tortuguita.right(180)
tortuguita.forward(50)
tortuguita.right(65)
tortuguita.forward(50)
b=tortuguita.pos()

#I
tortuguita.goto(b)
tortuguita.right(-65)
tortuguita.pencolor("blue")
tortuguita.pensize(30)
tortuguita.shape("circle")
tortuguita.forward(110)
tortuguita.forward(-60)
tortuguita.left(90)
tortuguita.forward(100)
tortuguita.left(90)
tortuguita.forward(50)
tortuguita.forward(-100)
tortuguita.penup()
tortuguita.goto(330, 0)
tortuguita.pendown()
tortuguita.goto(330, -10)
c=tortuguita.pos()

#M
tortuguita.goto(c)
tortuguita.right(180)
tortuguita.pencolor("red")
tortuguita.pensize(28)
tortuguita.shape("turtle")
tortuguita.left(90)
tortuguita.forward(100)
tortuguita.right(130)
tortuguita.forward(100)
tortuguita.left(100)
tortuguita.forward(100)
tortuguita.right(130)
tortuguita.forward(0)
tortuguita.goto(489, 0)
tortuguita.pendown()
tortuguita.goto(527, 100)
d=tortuguita.pos()

#E
tortuguita.goto(d)
tortuguita.right(-70)
tortuguita.pensize(30)
tortuguita.pencolor("black")
tortuguita.forward(70)
tortuguita.backward(90)
tortuguita.right(90)
tortuguita.forward(70)
tortuguita.left(90)
tortuguita.forward(90)
tortuguita.backward(90)
tortuguita.right(90)
tortuguita.forward(70)
tortuguita.left(90)
tortuguita.forward(10)
tortuguita.forward(80)
e=tortuguita.pos()
#JAIME