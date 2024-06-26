from player import user


class Item:

  def __init__(self, name, damage, dialogue, temp, description):
    self.name = name
    self.damage = damage
    self.dialogue = dialogue
    self.temp = temp
    self.description = description
    


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
                 1,
                 """A potion filled with magic that can gravely wound an enemy.""")


heal_potion = Item("Healing Potion",
                  -50,
                  """You drink the potion. Your wounds fade 
and weariness leaves your body.""",
                  1,
                  """A potion that can heal """)


stick = Item("Pointy Stick",
            5,
            """You poke the enemy with your stick!""",
            0)


sword = Item("Sword",
            10,
            """You unsheathe your sword and slash at the enemy!""",
            0)


gold_sword = Item("Golden Sword",
                 15,
                 """You cut down the enemy with arcane powers!""",
                 0)



        
        