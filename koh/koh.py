import turtle

lenght = input("Введите длинну отрезка: ")
n = input("Введите количество итераций: ")

turtle.shape('turtle')
window = turtle.Screen()
window.setup(width=800, height=600, startx=200, starty=50)
# window.bgcolor("orange")
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
turtle.write("Алексей Белан,  34 группа , Кривая Коха", move=False, align="center",
             font=("Times New Roman", 16, "normal"))
turtle.penup()
turtle.goto(-380, -200)
turtle.pendown()
turtle.pensize(1)
turtle.speed(0)


def Koch_Line(len, n):
    if n == 0:
        turtle.forward(len)
        return
    # len //= 3
    len = len / 3
    Koch_Line(len, n - 1)
    turtle.left(60)
    Koch_Line(len, n - 1)
    turtle.right(120)
    Koch_Line(len, n - 1)
    turtle.left(60)
    Koch_Line(len, n - 1)


Koch_Line(int(lenght), int(n))

window.exitonclick()
