import turtle


def draw_partial_fern(t, size, angle, c1, c2):
    t.left(angle)
    draw_fern(t, size * c1)
    t.right(angle)
    t.backward(size * c2)


def draw_fern(t, size):
    if size > 1:
        t.forward(size)
        draw_partial_fern(t, size, 10, 0.8, 0.05)
        draw_partial_fern(t, size, -45, 0.45, 0.2)
        draw_partial_fern(t, size, 45, 0.4, 0.75)
        window.update()


window = turtle.Screen()
window.setup(width=800, height=600, startx=200, starty=50)

fr = turtle.Turtle()
fr.hideturtle()
fr.color("black")
fr.penup()
fr.goto(0, 250)
fr.pendown()
fr.write("Алексей Белан,  34 группа , Папоротник Барнсли ", move=False, align="center",
         font=("Times New Roman", 16, "normal"))
fr.pensize(1)
fr.speed(0)
fr.penup()
fr.goto(0, -250)
fr.pendown()
fr.left(90)
window.tracer(False)
draw_fern(fr, 100)
window.tracer(True)
window.exitonclick()
