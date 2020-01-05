
from ItemBase import BaseItem


class Chr:

    def __init__(self, health, InvSpace, alive):
        self.health = health
        self.InvSpace = InvSpace
        self.alive = alive

    def pickup(self, InvSpace):
        if BaseItem:
            BaseItem - InvSpace
            print("picked up an item!")
        else:
            print("")






















