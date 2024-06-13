import random
from getkey import getkey

import items
import inventory as inv
from player import user
from tabulate import tabulate


dodgeoptions = ["w", "a", "s", "d"]


def dodgewarning(dodge):
  """Contains code that will print which direction
  the player needs to dodge"""
  if dodge == "w":
    print("UP")
  elif dodge == "a":
    print("LEFT")
  elif dodge == "d":
    print("RIGHT")
  else:
    print("DOWN")


class Enemy():

    def __init__(self, health, timer, damage):
        self.health = health
        self.timer = timer
        self.damage = damage

  
    def slow_attack(self):
        """Contains the code for a slower attack"""
        stored_time = self.timer
        dodge = random.choice(dodgeoptions)
        while self.timer > 0:
            time.sleep(2)
            self.timer -= 1
            if self.timer == 6:
                dodgewarning(dodge)
                start = time.time()
                dodge_attempt = getkey()
            if attempt == dodge:
                if end - start < 1:
                    dodge = 2
                else:
                    dodge = 0
                break
            elif attempt != dodge:
                dodge = 1
                break
        if dodge != 2:
            
                    print("You failed to dodge the attack in time!")
                    print(f"You took {self.damage} damage!")
            elif dodge == 1:
                    print("You dodged in the wrong direction!")
                    print(f"You took {self.damage} damage!")
        else:
            print("You managed to dodge the attack!")

    

    def write_healthtable(self):
        """ """
        try:
            with open('health.txt', "w") as file:
                file.write(tabulate(["Player",
                                    tablefmt = 'simple_grid'))
        except:
            print("Can't count your health")
        else:
            print("Your health is noted")
        finally:
            print("Pay attention ")

    def read_health(self):
        try:
            with open('health.txt', "r") as file:
                print(file.read())
        except:
            print("Can't read your health")
        else:
            print("You're viewing your health")
        finally:
            print("Be careful !!")

    def combat(self):
        """ Codes for using the items in the inventory"""
        print("\n")
        combatchoice = input("Choose an item: ").lower()
        if (combatchoice == "damage potion" 
            and items.dmg_potion in inv.inventory.inventory):
            items.dmg_potion.itemuse(self.health)
            del items.dmg_potion
        elif (combatchoice == "healing potion"
              and items.heal_potion in inv.inventory.inventory):
            items.heal_potion.itemuse(self.health)
            del items.heal_potion
        elif combatchoice == "chicken":
            items.chicken.itemuse(self.health)
            del items.chicken
        #elif combatchoice == "pointy stick":
        else:
            print("You don't have this item.")