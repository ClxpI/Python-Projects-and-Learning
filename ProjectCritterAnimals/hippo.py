# This class represents a Hippo type of Critter
# It moves 5 times at the direction choosen randomly. It eats when hungry and scratches if hungry or punces if not hungry for an attack.
# it is represented by a gray 5

import random
from critter import *

class Hippo (Critter):
    def __init__(self, hunger):
        super(Hippo, self).__init__() # You can set the attribute to any the class is determine with
        self.alternate = 0 # attribute is zero when set which is utilised to change directions
        self.hunger = 0 # hunger is set to zero
    
    def eat(self):
        if self.hunger != 0: # if hunger is not equal to zero hippo will eat
            self.hunger = self.hunger - 1 # reduces value by 1 of hunger so eventually it will become 0
            return True
        else:
            return False # if false is returned then hippo won't eat.
    
    def fight(self, opponent):
        if self.hunger != 0:
            return ATTACK_SCRATCH # ATTACK_SCRATCH is set to scratch
        else:
            return ATTACK_POUNCE # ATTACK_POUNCE is set to pounce
    
    def get_color(self):
        if self.hunger != 0: # if hippo is hungry color will be gray otherwise it will be white
            return "gray"
        else:
            return "white"
  
    def get_move(self):
        if self.alternate == 0:
            self.alternate = random.randint(1,4) # if self.alernate is set to 0 it will generate a new number from 1-4 and set it to self.aletrnate
            if self.alternate == 1:
                for i in range(1,5):
                    i = i + 1
                    self.alternate = 0 # sets value of self.alternate back to zero 
                    return DIRECTION_NORTH # if self.aletrante value is 1 it will move north 5 times
            elif self.alternate == 2:
                for i in range(1,5):
                    i = i + 1
                    self.alternate = 0 # sets value of self.alternate back to zero 
                    return DIRECTION_EAST # if self.aletrante value is 2 it will move east 5 times
            elif self.alternate == 3:
                for i in range(1,5):
                    i = i + 1
                    self.alternate = 0 # sets value of self.alternate back to zero 
                    return DIRECTION_SOUTH # if self.aletrante value is 3 it will move south 5 times
            else:
                for i in range(1,5):
                    i = i + 1
                    self.alternate = 0 # sets value of self.alternate back to zero 
                    return DIRECTION_WEST # if self.aletrante value is 4 it will move west 5 times
                
    
    def __str__(self):
        hippohunger = str(self.hunger)
        return "5"  # hippo shape is set as 5

