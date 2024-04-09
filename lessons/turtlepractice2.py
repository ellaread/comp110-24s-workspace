from turtle import Turtle, done

def draw_branch(branch_length, t: Turtle):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_branch(branch_length - 15, t)
        t.left(40)
        draw_branch(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

def main():

    t: Turtle = Turtle()
    t.speed(0)
    t.color("green")
    t.width(2)

    t.left(90)
    t.up()
    t.backward(100)
    t.down()

    draw_branch(100, t)


if __name__ == "__main__":
    main()