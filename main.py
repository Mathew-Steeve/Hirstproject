import turtle as t
import random
t.colormode(255)

colors = [(219, 254, 237), (84, 254, 155), (173, 146, 118), (245, 39, 191), (158, 107, 56), (2, 1, 176), (151, 54, 251),
          (221, 254, 101), (253, 146, 193), (3, 87, 176), (249, 1, 246), (35, 34, 253), (1, 213, 212), (249, 0, 0),
          (254, 147, 146), (253, 71, 70), (244, 248, 254), (39, 249, 42), (85, 249, 253), (240, 1, 13), (5, 210, 216),
          (230, 126, 190), (2, 2, 107), (135, 152, 220), (174, 162, 249), (208, 118, 26), (253, 7, 4), (248, 6, 19)]
t.up()
t.setpos(0, -150)
t.hideturtle()


def random_color():
    cr = random.choice(colors)
    r = cr[0]
    g = cr[1]
    b = cr[2]
    rand_color = (r, g, b)
    return rand_color


def movement():
    for _ in range(10):
        t.dot(20, random_color())
        t.forward(50)


for m in range(10):
    movement()
    t.left(90)
    t.forward(50)
    t.right(90)
    t.setpos(0, (m-2)*50)

screen = t.Screen()
screen.exitonclick()
