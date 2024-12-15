# This class represents a WildCat type of Critter
# It it moves north twice, then east twice, then south twice and then west twice. It always eats and pounces as attack. 
# it is represented by a green £

from critter import *

class Wildcat1(Critter):
    def __init__(self):
        super(Wildcat1, self).__init__()
        self.last = "none" # attribute is zero when set which is utilised to change directions
        self.north = 0 # attribute is zero when set which is utilised to change directions
        self.east = 0 # attribute is zero when set which is utilised to change directions
        self.south = 0 # attribute is zero when set which is utilised to change directions
        self.west = 0 # attribute is zero when set which is utilised to change directions

    def eat(self):
        return True # wildcat is always hungry

    def fight(self, opponent):
        return ATTACK_POUNCE # ATTACK_POUNCE is set to pounce
    
    def get_color(self):
        return "green" # sets the color to green
  
    def get_move(self):
        if self.north < 5:
            self.north = self.north + 3
            self.last = "North"
            return DIRECTION_NORTH # When it's set to 3 next time, it will travel north
        elif self.north == 5:
            self.east = self.east + 2
            self.north = self.north + 5
            self.last = "East"
            return DIRECTION_EAST # When it's set to 5 next time, it will travel east
        elif self.east < 3:
            self.east = self.east + 2
            self.last = "East"
            return DIRECTION_EAST # When it's set to 7 next time, it will travel east
        elif self.east == 3:
            self.south = self.south + 7
            self.east = self.east + 2
            self.last = "South" 
            return DIRECTION_SOUTH # When it's set to 7 next time, it will travel south
        elif self.south < 3:
            self.south = self.south + 7
            self.last = "South"
            return DIRECTION_SOUTH # When it's set to 6 next time, it will travel south
        elif self.south == 3:
            self.west = self.west + 6
            self.south = self.south + 7
            self.last = "West"
            return DIRECTION_WEST # When it's set to 6 next time, it will travel west
        else:
            self.north = 1
            self.east = 3
            self.south = 5
            self.west = 4
            self.last = "North"
            return DIRECTION_NORTH # When it's set to 3 next time, it will travel north


    def __str__(self):
        return"£" #sets the shape of wildcat
   


