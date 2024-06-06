import sys

import map


class Player:

    def __init__(self, health, x_loc, y_loc, area):
        # Contains the statistics and location of the player
        self.health = health
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.area = area
        self.action = ["move", "map", "inventory", "search", "quit"]


    def describeroom(self):
        """Code that prints the description of the room 
        that the player is currently in"""
        # Finds which room the player is in
        rooms = self.area[self.y_loc][self.x_loc]
        print("\n")
        # That room's description is then printed
        print(rooms.description)
        print('\n')


    def movement(self, playerchoice):
        """Contains the code that prints the movement options for the player
        and allows the player to be able to move around the map"""
        # All the valid options the player has for movement
        print("\n")
        MoveOptions = ["w", "a" ,"s" ,"d" ,"e", "r"]
        r_check = 0
        # Plays the loop so long as a valid choice has not been selected
        while playerchoice == "N/A":
            try:
                # Checks if the player is unable to move in a direction
                # If so then the option for the room does not print
                if self.x_loc != 0:
                    print("a - Move Left")
                if self.x_loc != 2:
                    print("d - Move Right")
                if self.y_loc != 0:
                    print("w - Move Up")
                if self.y_loc != 2:
                    print("s - Move Down")
                if (self.area == map.plain_map 
                    and self.y_loc == 0
                    and self.x_loc == 2):
                    print("r - Enter Lair")
                    r_check = 1
                elif (self.area == map.tower_map
                     and self.y_loc == 2
                     and self.x_loc == 2):
                    print("r - Exit Lair")
                    r_check = 1
                # Prints the option to exit movement
                print("e - Quit")
                # Player then inputs their choice 
                playerchoice = input("""Type the letter to choose the
option: """).lower()
                print("\n")
                # The input is tested to see if it's a number
                playerchoice = float(playerchoice)
            # A ValueError indicates a string type
            except ValueError:
                # Checks if the player's choice was valid
                if playerchoice not in MoveOptions:
                    # If not then an error message is displayed and the 
                    # loop continues
                    print("Input a letter from the options")
                    playerchoice = "N/A"
            # No ValueError indicates a numerical value
            else:
                # An error is displayed and the loop continues
                print("Don't type a number")
                playerchoice = "N/A"
            finally:
                # Checks if the player can move in that direction
                # If the player is on the edges of the map, the movement fails
                if ((self.x_loc == 0 and playerchoice == "a")
                    or (self.x_loc == 2 and playerchoice == "d")
                    or (self.y_loc == 0 and playerchoice == "w")
                    or (self.y_loc == 2 and playerchoice == "s")):
                    print("Can't move in that direction")
                    playerchoice = "N/A"
                # Checks if the loop is going to continue
                if playerchoice == "N/A":
                    # If so then the player is told that the movement failed
                    print("Movement Failed!")
                    print("\n")
                # Otherwise the player's location is changed
                else:
                    # Checks if the player wants to move left
                    if playerchoice == "a":
                        # The player is moved 1 room to the left
                        self.x_loc = self.x_loc - 1
                        print("Moving Left")
                    # Checks if the player wants to move right
                    elif playerchoice == "d":
                        # The player is moved 1 room to the right
                        self.x_loc = self.x_loc + 1
                        print("Moving Right")
                    # Checks if the player wants to move up
                    elif playerchoice == "w":
                        # The player is moved 1 room up
                        self.y_loc = self.y_loc - 1
                        print("Moving Up")
                    # Checks if the player wants to move down
                    elif playerchoice == "s":
                        # The player is moved 1 room down
                        self.y_loc = self.y_loc + 1
                        print("Moving Down")
                    # Check if player wants to exit game
                    elif playerchoice == "e":
                        # Thank you message will be printed
                        sys.exit("Thank you for playing")
                    # Check if player wants to enter the tower
                    elif playerchoice == "r" and r_check == 1:
                        # If the player is entering the tower
                        if self.area == map.plain_map:
                            # The player's location and area are switched
                            self.area = map.tower_map
                            self.x_loc = 2
                            self.y_loc = 2
                        # Otherwise the player is exiting the tower
                        else:
                            # The player's location and area are switched
                            self.area = map.plain_map
                            self.x_loc = 2
                            self.y_loc = 0
                    # Returns playerchoice for the treasure room check
                    return playerchoice


user = Player(100, 1, 2, map.plain_map)

