# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# print(timmy)
#
# timmy.shape("turtle")
# timmy.color("coral", "red")
# timmy.forward(100)
# timmy.left(45)
# timmy.forward(100)
#
# my_screen = Screen()
#
# print(my_screen.canvheight)
#
# my_screen.exitonclick()
#

from prettytable import PrettyTable

table = PrettyTable()
# table.field_names = ["Pokemon name", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])

table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["ELectric", "Water", "Fire"])

table.align = "l"

print(table)


