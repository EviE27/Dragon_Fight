from tabulate import tabulate


class Map:
    
    def __init__(self, map, external_file):
        self.map = map
        self.mapfile = external_file
        
    def WriteMap(self):
        ''' The function writes map to an external file.'''
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
        ''' The function reads and prints map from an
        external file.
        '''
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
        ''' The function contains functions that write 
        and read map.
        '''
        self.WriteMap()
        self.ReadMap()


class Room:
    def __init__(self, description):
        self.description = description


# Rooms for plain map
armory = Room("")
forest = Room("")
town = Room("")
bar = Room("")
beware = Room("")
start = Room("")
entrance = Room("")
brewery = Room("")
library = Room("")

# Rooms for tower map
stairs = Room("")
hallway = Room("")
wizard = Room("")
treasure = Room("")
map = Room("")
kitchen = Room("")
grunt = Room("")
entrance1 = Room("")

# Arrays of rooms
plain_map = [
    [armory, bar, entrance],
    [forest, beware, brewery],
    [town, start, library]
]

tower_map = [
    [stairs, treasure, grunt],
    [hallway, map, hallway],
    [wizard, kitchen, entrance1]
]

# Arrays of map 
plainmap = [
    ["armory", "bar", "entrance"],
    ["forest", "beware", "brewery"],
    ["town", "start", "library"]
]

towermap = [
    ["stairs", "treasure", "grunt"],
    ["hallway", "map", "hallway"],
    ["wizard", "kitchen", "entrance"]
]

# Create map objects
map1 = Map(plainmap, 'plain_map.txt')
map2 = Map(towermap, 'tower_map.txt')