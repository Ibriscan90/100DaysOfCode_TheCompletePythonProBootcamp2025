# import turtle
#
#
# timmy = turtle.Turtle()
# timmy.shape('turtle')
# timmy.color('green')
# timmy.forward(100)
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name', ["Pikachu", "Squirtle", "Charmander"])
table.add_column('Type', ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)


