#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Title: Dragon Fight!
# Class: Computer Science 30
# Assignment: Capstone Coding Project
# Programmers: Sami Shahab, Eve Olson, Suri Ho
# Version: v3.0
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import sys

import items
import map
from inventory import inventory, treasureroom
from player import user


def main_menu():
    # Loops the game
    while True:
        # Describes the room the player is in
        user.describeroom()
        # Loop is started
        loop = "Y"
        while loop == "Y":
            # Prints out the player's movement options
            print("\n")
            for action in user.action:
                print(f"-{action}")
            # Player can choose from the above options
            user_input = input("Choose an action: ").lower()
            # If the player chooses to move, the movement function will run
            if user_input == "move":
                check = user.movement("N/A")
                # Check if player has the key to enter treasure room
                if (user.area[user.y_loc][user.x_loc] == map.treasure
                    and items.key not in inventory.inventory):
                    # If not then this function runs
                    treasureroom(check)
                # The loop ends, allowing the room description to be printed
                loop = "N"
            # Otherwise if the player chooses map, the map will be printed
            elif user_input == "map":
                # Checks which map the player is currently in
                if user.area == map.plain_map:
                    map.map1.ShowMap()
                else:
                    map.map2.ShowMap()
            # If player choose inventory, inventory's items will be printed
            elif user_input == "inventory":
                inventory.view_inventory()
            # If player choose search, searchroom function will run
            elif user_input == "search":
                inventory.searchroom()
            # If player chooses quit, the game will stop
            elif user_input == "quit":
                sys.exit("Thank you for playing.")
            # Invalid action error
            else:
                print("Choose a valid action.")


main_menu()