import map

class Inventory:

    def __init__(self):
        self.inventory = []
        
    def view_inventory(self):
        """Contains codes that allow player to view their inventory"""
        # Print out items if player has something in inventory
        if self.inventory:
            print("Inventory: ")
            for item in self.inventory:
                print(f"-{item}")
        else:
            print("You have nothing in your inventory.")


    def searchroom(self):
        """Code for searching rooms"""
        try:
            self.inventory.append()