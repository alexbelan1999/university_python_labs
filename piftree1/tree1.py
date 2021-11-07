import math
import turtle

lenght = int(input("Введите длинну отрезка: "))
n = int(input("Введите n: "))
alfa = int(input("Введите альфа: "))
beta = 90 - alfa

window = turtle.Screen()
window.setup(width=800, height=600, startx=200, starty=50)
window = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(0, 250)
t.pendown()
t.write("Алексей Белан,  34 группа , Классическое дерево Пифагора", move=False, align="center",
        font=("Times New Roman", 16, "normal"))
t.pensize(1)
t.speed(1)
t.penup()
t.goto(-75, -275)
t.pendown()


def fractal(aturt, length, depth, maxdepth):
    if depth > maxdepth:
        return
    length1 = length * math.sin(math.radians(alfa))
    length2 = length * math.sin(math.radians(beta))

    aturt.color("green")
    anotherturt = aturt.clone()
    anotherturt.color("blue")
    aturt.forward(length)
    aturt.left(alfa)
    fractal(aturt, length2, depth + 1, maxdepth)
    anotherturt.right(90)
    anotherturt.forward(length)
    anotherturt.left(90)
    anotherturt.forward(length)
    if depth != maxdepth:
        turt3 = anotherturt.clone()
        turt3.color("yellow")
        turt3.left(alfa)
        turt3.forward(length1)
        turt3.right(90)
        fractal(turt3, length1, depth + 1, maxdepth)
    anotherturt.left(90)
    anotherturt.forward(length)


t.left(90)
fractal(t, lenght, 1, n)
window.exitonclick()
