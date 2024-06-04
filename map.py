from tabulate import tabulate


class Map:
    
    def __init__(self, map, external_file):
        self.map = map
        self.mapfile = external_file
        
    def WriteMap(self):
        """The function writes map to an external file."""
        try:
            with open(self.mapfile,"w") as file:
                file.write(tabulate(self.map, tablefmt = 'fancy_grid'))
        except:
            print("Failed to write map!")
        else:
            print("Map has been created.")
        finally:
            print("Let's explore!")
            
    def ReadMap(self):
        """The function reads and prints map from an external file."""
        try:
            with open(self.mapfile, "r") as file:
                print(file.read())
        except:
            print("Oh! Can't read the map.")
        else:
            print("Here's the map.")
        finally:
            print("Good luck!!")
            
    def ShowMap(self):
        """Contains functions that write and read map."""
        self.WriteMap()
        self.ReadMap()


class Room:
    def __init__(self, description):
        self.description = description


# Rooms for plain map
armory = Room("You have entered the Armory.")
forest = Room("You are in the dark forest.")
town = Room("You are walking through the small town.")
bar = Room("You enter the local bar. It looks like theres a fight.")
beware = Room("You stumbel across a warning. Beware the dragon in the tower.")
start = Room("")
entrance = Room("""You approch the tall stone tower.
The tower has a giant woodend door with thick metal bars over it.""")
brewery = Room("""You walked into the magical brewery.
The room is filled with potions and magical ingredients.
In the middel of the room there is a large stone pot.""")
library = Room("""You enter the library. 
everywhere you look there are shelves upon shelves of magical books""")

# Rooms for tower map
stairs = Room("""You are walking up a flight of stairs and
Woosh the dragon flys in!""")
hallway = Room("You are traveling down the cold, stone, candle lit hallway")
wizard = Room("It looks like you have entered some type of dungen or is it")
treasure = Room("""You made it to the treasure room!
Everywhere you look there are piles upon piles of treasure.""")
kitchen = Room("""You smell the sweet smell of fryed chiken. 
You have wondered into KFC.""")
grunt = Room("You are in the grunt room. Get ready to fight.")
entrance1 = Room("You have entered the tower. Be careful ")

# Arrays of rooms for moving
plain_map = [
    [armory, bar, entrance],
    [forest, beware, brewery],
    [town, start, library]
]

tower_map = [
    [stairs, treasure, grunt],
    [hallway, hallway, hallway],
    [wizard, kitchen, entrance1]
]

# Arrays of map for printing
plainmap = [
    ["armory", "bar", "entrance"],
    ["forest", "beware", "brewery"],
    ["town", "start", "library"]
]

towermap = [
    ["stairs", "treasure", "grunt"],
    ["hallway", "hallway", "hallway"],
    ["wizard", "kitchen", "entrance"]
]

# Create map objects
map1 = Map(plainmap, 'plain_map.txt')
map2 = Map(towermap, 'tower_map.txt')