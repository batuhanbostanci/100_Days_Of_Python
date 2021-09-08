

#from turtle import Turtle, Screen
# timmy = Turtle()
# my_screen = Screen()
#
# timmy.shape("turtle")
# timmy.color()
# timmy.forward(100)

from prettytable import PrettyTable


table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.align = "l"
print(table)

table2 = PrettyTable()
table2.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table2.add_column("Type", ["Electric", "Water", "Fire"])

print(table2)