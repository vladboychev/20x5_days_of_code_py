import turtle as t
import random as r
pit = t.Turtle()
pit.penup()
pit.hideturtle()
t.colormode(255)


def color_list_from_jpg(picture, number_of_colors):
    import colorgram as cg
    rgb_colors = []
    colors = cg.extract(picture, number_of_colors)
    for color in colors:
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.b
        rgb_colors.append((red, green, blue))
    return rgb_colors


color_list = color_list_from_jpg("pic.jpg", 50)


def clean_color_list(lst):
    a_lst = []
    for tup in lst:
        a_lst.append(list(tup))
    # print(a_lst)
    b_lst = []
    for a in a_lst:
        if sum(a) < 600 or sum(a) > 150:
            b_lst.append(a)
    return [tuple(b) for b in b_lst]


def random_color(lst):
    return r.choice(lst)


pit.setposition(-230, -230)

for i in range(-230, 270, 50):
    for j in range(-230, 270, 50):
        pit.dot(20, random_color(color_list))
        pit.setposition(i, j)

pit.setposition(220, 220)
pit.dot(20, random_color(color_list))
screen = t.Screen()
screen.exitonclick()
