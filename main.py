#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Title: Dragon Fight!
# Class: Computer Science 30
# Assignment: Capstone Coding Project
# Programmers: Sami Shahab, Eve Olson, Suri Ho
# Version: v0.1
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from player import user


def main_menu():
    while True:
        user.describeroom()
        user.movement("N/A")


main_menu()