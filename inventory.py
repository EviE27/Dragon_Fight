import items
import map
from player import user


class Inventory:

    def __init__(self):
        self.inventory = [items.stick]
        
    def view_inventory(self):
        """Contains codes that allow player to view their inventory"""
        # Print out items if player has something in inventory
        if self.inventory:
            print("\n")
            print("Inventory: ")
            for item in self.inventory:
                print(f"-{item.name}")
        # Otherwise this message prints
        else:
            print("You have nothing in your inventory.")

    def searchroom(self):
        """Code for searching rooms"""
        try:
            # Checks which area the player is in
            plain = 0
            if user.area == map.plain_map:
                # The items in the arrays match up to the map array
                # Due to this, the players location will match up to 
                # the correct item
                item = items.plains_items[user.y_loc][user.x_loc]
                plain = 1
            else:
                item = items.tower_items[user.y_loc][user.x_loc]
            # If the item is not "N/A", the item is added to the 
            # player's inventory
            if item != "N/A":
                    self.inventory.append(item)
                    print("\n")
                    print(f"You found {item.name}!")
                    print(f"You put {item.name} away in your inventory!")
                    if plain == 1:
                        items.plains_items[user.y_loc][user.x_loc] = "N/A"
                    else:
                        items.tower_items[user.y_loc][user.x_loc] = "N/A"
            # Otherwise this text prints
            else:
                print("Nothing notable in here...")
        # In the event of an error, this text is printed
        except:
            print("""While you were searching, you tripped and stubbed
your toe.""")
            print("YEOOOOOOOOWWWCH")
        finally:
            # A message to indicate to the player that the search is complete
            print("\n")
            print("Search complete!")


inventory = Inventory()


def treasureroom(playerchoice):
    """Act as the lock for the treasure room"""
    # Pushes the player back to where they initially came from
    if playerchoice == "w":
            user.y_loc = user.y_loc + 1
    elif playerchoice == "a":
            user.x_loc = user.x_loc + 1
    elif playerchoice == "d":
            user.x_loc = user.x_loc - 1
    print("\n")
    print("You seem to be missing the key to this room...")