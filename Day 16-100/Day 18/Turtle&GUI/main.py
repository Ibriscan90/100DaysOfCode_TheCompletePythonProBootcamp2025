import random
import turtle as t


tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rcolor = (r,g,b)
    return rcolor

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

#colors = ["Indigo", "DeepPink", "Yellow", "GreenYellow", "DeepSkyBlue"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

# directions = [0, 90, 180, 270]
# tim.pensize(15)
tim.speed('fastest')
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# for _ in range(200):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.left(10)

def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(50)
        tim.setheading(tim.heading() + gap_size)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()


