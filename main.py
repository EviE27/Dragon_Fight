#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Title: Dragon Fight!
# Class: Computer Science 30
# Assignment: Capstone Coding Project
# Programmers: Sami Shahab, Eve Olson, Suri Ho
# Version: v3.0
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import sys

import map
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
                user.movement("N/A")
                # The loop ends, allowing the room description to be printed
                loop = "N"
            # Otherwise if the player chooses map, the map will be printed
            elif user_input == "map":
                # Checks which map the player is currently in
                if user.area == map.plain_map:
                    map.map1.ShowMap()
                else:
                    map.map2.ShowMap()
            # If player chooses quit, the game will stop
            elif user_input == "quit":
                sys.exit("Thank you for playing.")
            # Invalid action error
            else:
                print("Choose a valid action.")


main_menu()