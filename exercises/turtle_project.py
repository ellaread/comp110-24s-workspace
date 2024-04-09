"""Flower Garden."""
"""Make use of dot function to fill in the center of flowers (above and beyond) line 78. Function flower is composed of three smaller functions and called on lines 82-98. Use loops in a clever way-- make a flower ln 40-43. Use a circle function from turtle website to make filled in hills line 121."""

from turtle import Turtle, colormode, done 
__author__ = "730487065"
colormode(255)

 
def main() -> None:
    """The entrypoint of my scene."""
    flower()
    t: Turtle = Turtle()
    t.speed(0)
    t.penup()
    t.goto(200, -100)
    t.left(90)
    t.backward(75)
    t.width(2)
    t.pendown()
    branch(75, t, (207, 207, 207))
    t.penup()
    t.goto(-150, -50)
    t.pendown()
    branch(65, t, (149, 214, 207))
    t.penup()
    hill(t, 350, -750, 500, 180, (150, 200, 150))
    hill(t, 100, -325, 200, 360, (150, 200, 150))
    done()


def bloom(t: Turtle, x: float, y: float, length1: float, color: tuple[int, int, int]) -> None:
    """Function to draw a flower blossom in the scene."""
    t.penup()
    t.goto(x, y)
    t.setheading(0.0)
    t.pendown()
    t.color(color)
    i: int = 0
    t.left(130)
    while i < 36:
        t.forward(length1)
        t.right(130)
        i = i + 1
    

def stem(t: Turtle, x: float, y: float, length1: float, color: tuple[int, int, int]) -> None:
    """Function to draw the stem of a flower."""
    t.penup()
    t.goto(x, y)
    t.setheading(270)
    t.pendown()
    t.color(color)
    t.begin_fill()
    i: int = 0
    while i < 6:
        t.forward(length1)
        t.right(80)
        t.forward(length1)
        t.left(160)
        t.forward(length1)
        t.right(80)
        t.forward(length1)
        t.left(80)
        t.forward(length1)
        t.right(160)
        t.forward(length1)
        t.left(80)
        i += 1
    t.end_fill()


def center(t: Turtle, x: float, y: float, size: int, color: tuple[int, int, int]) -> None:
    """Function to create center of flower."""
    t.penup()
    t.goto(x, y)
    t.fillcolor(color)
    t.pendown()
    t.dot(size)
    t.penup()
    

def flower() -> None:
    """Function to incorporate multiple functions and draw entire flower."""
    t: Turtle = Turtle()
    t.speed(0)
    t.hideturtle()
    bloom(t, -200, -100, 90, (170, 231, 250))  # blue flower
    stem(t, -200, -100, 15, (170, 231, 250))
    center(t, -212.75, -52.25, 40, (170, 231, 250))
    bloom(t, -100, -130, 70, (234, 131, 102))  # orange flower
    stem(t, -100, -130, 15, (234, 131, 102))
    center(t, -110, -92.25, 31, (234, 131, 102))
    bloom(t, -50, -50, 100, (252, 193, 244))   # pink flower
    stem(t, -50, -50, 18, (252, 193, 244))
    center(t, -64.5, 3.5, 45, (252, 193, 244))
    bloom(t, 50, -100, 80, (166, 219, 173))   # green flower
    stem(t, 50, -100, 17, (166, 219, 173))
    center(t, 39, -57.5, 36, (166, 219, 173))


def branch(branch_length: float, t: Turtle, color: tuple[int, int, int]) -> None:  # I used tuples instead of my initial list[int] because gradescope was giving type safety errors.
    """Create recursive/fractal tree branches."""
    t.color(color)
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        branch(branch_length - 10, t, color)
        t.left(40)
        branch(branch_length - 10, t, color)
        t.right(20)
        t.backward(branch_length)


def hill(t: Turtle, x: float, y: float, radius: float, range: float, color: tuple[int, int, int]) -> None:
    """Function to create rolling hills in the foreground."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius, range)
    t.end_fill()
    t.penup()


if __name__ == "__main__":
    main()