from tabulate import tabulate


class Map:
    
    def __init__(self, map, external_file):
        self.map = map
        self.mapfile = external_file
        
    def WriteMap(self):
        try:
            with open(self.mapfile,"w") as file:
                file.write(tabulate(self.map, tablefmt = 'fancy_grid'))
        except:
            print("")
        else:
            print("")
        finally:
            print("")
            
    def ReadMap(self):
        try:
            with open(self.mapfile, "r") as file:
                print(file.read())
        except:
            print("")
        else:
            print("")
        finally:
            print("")
            
    def ShowMap(self):
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

plain_map = [
    [armory, bar, entrance],
    [forest, beware, brewery],
    [town, start, library]
]

tower_map = [
    [stairs, treasure, grunt],
    [hallway, map, hallway],
    [wizard, kitchen, entrance]
]

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