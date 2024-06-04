from player import user


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
            room = user.area[user.y_loc][user.x_loc]
            if room.item != "N/A":
                    self.inventory.append(room.item)
                    print(f"You found {room.item}!")
                    print(f"You put {room.item} away in your inventory!")
        except:
            print("Nothing notable in here...")
        finally:
            print("\n")
            print("Search complete!")
            print("\n")
            