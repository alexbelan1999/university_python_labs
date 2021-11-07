import turtle

lenght = int(input("Введите длинну отрезка: "))
alfa = int(input("Введите альфа: "))
beta = 90 - alfa
k = float(input("Введите k: "))
turtle.hideturtle()
window = turtle.Screen()
window.setup(width=800, height=600, startx=200, starty=50)
turtle.penup()
turtle.goto(0, 250)
turtle.pendown()
turtle.write("Алексей Белан,  34 группа , «Обнаженное» дерево Пифагора ", move=False, align="center",
             font=("Times New Roman", 16, "normal"))
turtle.pensize(1)
turtle.speed(0)
turtle.penup()
turtle.goto(0, -250)
turtle.pendown()


def tree(f_lenght, min_lenght=10):
    turtle.forward(f_lenght)
    if f_lenght > min_lenght:
        turtle.left(alfa)
        tree(k * f_lenght, min_lenght)
        turtle.right(90)
        tree(k * f_lenght, min_lenght)
        turtle.left(beta)
    turtle.back(f_lenght)


turtle.left(90)
tree(lenght)
window.exitonclick()
