# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# #the object is my_screen
# my_screen = Screen()
# #canvheight is the attribute that's associated with that sreen
# print(my_screen.canvheight)
# #exitonclick is a method
# my_screen.exitonclick()

from prettytable import PrettyTable #PrettyTable is a class
#create a nwew object called table
table = PrettyTable()
table.add_column("Pokemone Name",["Pancham","Charizard","Wartortle"])
table.add_column("Type",["Poison","Water","Eletric"])
table.align = "r"
print(table)


