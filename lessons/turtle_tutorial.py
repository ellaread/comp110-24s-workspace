from turtle import Turtle, colormode, done

colormode(255)
leo: Turtle = Turtle()
leo.color("light blue", "blue")
leo.speed(50)
leo.hideturtle()
leo.penup()
leo.goto(-150,-150)
leo.pendown()
leo.begin_fill()
i: int = 0
side_length: int = 300 
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()
bob.pencolor(183, 236, 180)
bob.speed(70)
bob.penup()
bob.goto(-150,-150)
bob.pendown()
while (i < 45):
    bob.forward(side_length * 0.96)
    bob.left(123)
    i = i + 1
done()