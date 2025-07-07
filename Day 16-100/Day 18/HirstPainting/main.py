import random
import turtle as t

import colorgram
import turtle as t

# colors = colorgram.extract("200430102527-01-damien-hirst-severed-spots.jpg",10)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.g
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

color_list = [(252, 250, 250), (253, 247, 247), (237, 251, 251), (249, 228, 228), (213, 13, 13), (198, 12, 12), (231, 228, 228), (197, 69, 69), (33, 90, 90), (43, 212, 212)]
t.colormode(255)
tim = t.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = t.Screen()
screen.exitonclick()