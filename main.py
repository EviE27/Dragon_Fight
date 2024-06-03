#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Title: Dragon Fight!
# Class: Computer Science 30
# Assignment: Capstone Coding Project
# Programmers: Sami Shahab, Eve Olson, Suri Ho
# Version: v0.1
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import map
from player import user


def main_menu():
    while True:
        user.describeroom()
        loop = "Y"
        while loop == "Y":
            print("\n")
            user_input = input("Choose an action: ")
            if user_input == "move":
                user.movement("N/A")
                loop = "N"
            elif user_input == "map":
                if user.area == map.plain_map:
                    map.map1.ShowMap()
                else:
                    map.map2.ShowMap()


main_menu()