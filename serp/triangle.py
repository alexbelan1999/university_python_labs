import turtle

n = int(input("Введите степень: "))

turtle.shape('turtle')
Turtle = turtle.Turtle()
window = turtle.Screen()
window.setup(width=800, height=600, startx=200, starty=50)
turtle.penup()
turtle.goto(0, 250)
turtle.pendown()
turtle.write("Алексей Белан,  34 группа , Треугольник Серпинского", move=False, align="center",
             font=("Times New Roman", 16, "normal"))
turtle.penup()
turtle.pensize(1)
turtle.speed(0)
turtle.hideturtle()
Points = [[-250, -200], [0, 200], [250, -200]]


def drawTriangle(points, color, Turtle):
    Turtle.fillcolor(color)
    Turtle.penup()
    Turtle.goto(points[0][0], points[0][1])
    Turtle.pendown()
    Turtle.shape('turtle')
    Turtle.begin_fill()
    Turtle.goto(points[1][0], points[1][1])
    Turtle.goto(points[2][0], points[2][1])
    Turtle.goto(points[0][0], points[0][1])
    Turtle.end_fill()


def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree, Turtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'gray', 'orange', 'brown', 'black', 'khaki']
    drawTriangle(points, colormap[degree], Turtle)
    if degree > 0:
        sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree - 1, Turtle)
        sierpinski([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])], degree - 1, Turtle)
        sierpinski([points[2], getMid(points[2], points[1]), getMid(points[0], points[2])], degree - 1, Turtle)
    else:
        return


sierpinski(Points, n, Turtle)
window.exitonclick()
