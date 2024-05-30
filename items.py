from player import user


class Item:

  def __init__(self, name, damage, dialogue):
    self.name = name
    self.damage = damage
    self.dialogue = dialogue


  def itemuse(self, enemyhealth):
    """Contains the code that handles how the items are used"""
    if self.damage > 0:
        try:
            enemyhealth = enemyhealth - self.damage
            print(self.dialogue)
        except ValueError:
            print("Who are you trying to attack?")
            print("You put the item away...")
        finally:
            print("\n")

    else:
        user.health = user.health - self.damage
        print(self.dialogue)


class DmgPotion(Item):
    super