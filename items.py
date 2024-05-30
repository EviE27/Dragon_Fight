from player import user


class Item:

  def __init__(self, name, damage, dialogue, temp):
    self.name = name
    self.damage = damage
    self.dialogue = dialogue
    self.temp = temp
    


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


dmg_potion = Item("Damage Potion",
                 20,
                 """You throw the potion at the enemy, causing it to burst open. 
Magical smog and glass wound the enemy!""",
                 1)


heal_potion = Item("Healing Potion",
                  -50,
                  """You drink the potion. Your wounds fade 
and weariness leaves your body.""",
                  1)






        
        