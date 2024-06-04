from player import user


class Item:
# Generic item class
  def __init__(self, name, damage, dialogue, temp, description):
    # Name of the item
    self.name = name
    # How much the item damages (or heals)
    self.damage = damage
    # Dialogue for using the item
    self.dialogue = dialogue
    # If the item is a 1 time use item
    self.temp = temp
    # Description of the item
    self.description = description
    


  def itemuse(self, enemyhealth):
    """Contains the code that handles how the items are used"""
    # Checks the if damage is positive
    if self.damage > 0:
        try:
            # If so then the item is used on an enemy
            enemyhealth = enemyhealth - self.damage
            print(self.dialogue)
        # Unless there is no current enemy
        except ValueError:
            # Then this dialogue prints
            print("Who are you trying to attack?")
            print("You put the item away...")
        finally:
            print("\n")
    else:
        # Otherwise if the damage is negative, the player heals
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
                  """A potion that can heal even the most major wounds""")


chicken = Item("Chicken",
              -25,
              """You eat the chicken and suddenly feel a lot better!""",
              1,
              """Some chicken that can heal minor wounds""")

stick = Item("Pointy Stick",
            5,
            """You poke the enemy with your stick!""",
            0,
            """A stick capable of dealing minor damage. 
It's not all that powerful. Still it's better than nothing.""")


sword = Item("Sword",
            10,
            """You unsheathe your sword and slash at the enemy!""",
            0,
            """A steel sword capable of dealing major damage.
An always reliable weapon favoured by many warriors.""")


gold_sword = Item("Golden Sword",
                 15,
                 """You cut down the enemy with arcane powers!""",
                 0,
                 """A golden sword capable of doing colossal damage.
A weapon enchanted with arcane powers to further boost it's strength""")

key = Item("Key",
          None,
          """You open the treasure room with the key.""",
          None,
          """A key that is specially designed for the treasure room.""")



        
        