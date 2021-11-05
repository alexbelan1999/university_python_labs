import turtle

# L-system set up
START = "fx"
RULES = {'x': 'x+yf+', 'y': '-fx-y', 'f': 'f', '+': '+', '-': '-'}

LEVEL = int(input("Введите кол-во итераций: ")) + 1

screen = turtle.Screen()
screen.tracer(False)
screen.setup(width=800, height=600, startx=200, starty=50)
turtle = turtle.Turtle(visible=False)
turtle.penup()
turtle.goto(0, 250)
turtle.pendown()
turtle.write("Алексей Белан,  34 группа , Кривая дракона ", move=False, align="center",
             font=("Times New Roman", 16, "normal"))
turtle.pensize(1)
turtle.speed(0)
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
turtle.left(90)
sub_string = string = START

for _ in range(LEVEL):
    turtle.pencolor("black")
    for character in sub_string:
        if character == '+':
            turtle.right(90)
        elif character == '-':
            turtle.left(90)
        elif character == 'f':
            turtle.forward(1)
    screen.update()

    full_string = "".join(RULES[character] for character in string)
    sub_string = full_string[len(string):]
    string = full_string

screen.tracer(True)
turtle.hideturtle()

screen.exitonclick()
