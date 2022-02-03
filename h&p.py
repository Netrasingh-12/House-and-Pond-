import turtle

cir = turtle.Turtle()
cir.begin_fill()
cir.color("blue")
cir.circle(100)
cir.end_fill()


import turtle

house = turtle.Turtle()

turtle.bgcolor("yellow")

#wall
house.begin_fill()
house.color("red")
for i in range(4):
    house.forward(100)
    house.left(90)

house.left(90)
house.forward(100)
house.end_fill()

    #roof
house.begin_fill()
house.color("pink")

house.right(30)
house.forward(100)
house.right(120)
house.forward(100)
house.end_fill()

#roof
house.begin_fill()
house.color("green")

house.right(30)
house.forward(100)
house.right(120)
house.forward(100)
house.end_fill()
    
turtle.done()
