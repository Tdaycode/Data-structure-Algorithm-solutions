# from turtle import Turtle, Screen
# tayo = Turtle()
# tayo.shape('turtle')
# tayo.color('coral')
# tayo.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column('City', ["Adelaide", "Brisbane", "Darwin"])
table.add_column('Type', ['Electric', 'water', 'fire'])
print(table)

