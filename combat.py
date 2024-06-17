import random
from getkey import getkey
import time

import items
import inventory as inv
from player import user
from tabulate import tabulate


dodgeoptions = ["w", "a", "s", "d"]


def dodgewarning(dodge):
    """Contains code that will print which direction
    the player needs to dodge
    """
    try:
        if dodge == "w":
                visual = "arrow_up.txt"
        elif dodge == "a":
                visual = "arrow_left.txt"
        elif dodge == "d":
                visual = "arrow_right.txt"
        else:
                visual = "arrow_down.txt"
        with open(visual, "r") as file:
                print(file.read())
    except:
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


    def randomattack(self):
        """Randomly determines the delay that the attack has"""
        attack_times = [2, 5, 7, 11, 16]
        self.timer = random.choice(attack_times)
    
  
    def enemy_attack(self):
        """Contains the code for a slower attack"""
        dodge = random.choice(dodgeoptions)
        while self.timer > 0:
            time.sleep(1)
            self.timer -= 1
            if self.timer == 1:
                dodgewarning(dodge)
                start = time.time()
                dodge_attempt = getkey()
            if dodge_attempt == dodge:
                if end - start < 1:
                    dodge = 2
                else:
                    dodge = 0
                break
            elif dodge_attempt != dodge:
                dodge = 1
                break
        if dodge != 2:
                if dodge == 0:
                    print("You failed to dodge the attack in time!")
                elif dodge == 1:
                    print("You dodged in the wrong direction!")
                user.health = user.health - self.damage
                print(f"You took {self.damage} damage!")
        else:
            print("You managed to dodge the attack!")


    def write_healthtable(self):
        """ """
        try:
            with open('health.txt', "w") as file:
                file.write(tabulate([["Player", user.health],
                                     ["Enemy", self.health]]))
        except:
            print("Can't see your health")
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
        elif (combatchoice == "healing potion"
              and items.heal_potion in inv.inventory.inventory):
            items.heal_potion.itemuse(self.health)
        elif (combatchoice == "chicken"
              and items.chicken in inv.inventory.inventory):
            items.chicken.itemuse(self.health)
        elif (combatchoice == "pointy stick"
              and items.stick in inv.inventory.inventory):
            items.stick.itemuse(self.health)
        elif (combatchoice == "sword"
              and items.sword in inv.inventory.inventory):
            items.sword.itemuse(self.health)
        elif (combatchoice == "golden sword"
              and items.gold_sword in inv.inventory.inventory):
            items.gold_sword.itemuse(self.health)
        else:
            print("You don't have this item.")