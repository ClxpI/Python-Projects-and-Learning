# This class represents a Ant type of Critter
# It stays still, doesn't eat and roars for an attack
# it is represented by a red %

from critter import *

class Ant (Critter):
    def __init__(self, walk_south):
        super(Ant, self).__init__()
        self.walk_south = walk_south # You can set the attribute to any the class is detrmine with 
        self.alternate = 0 # attribute is zero when set which is utilised to change directions       
    

    def eat(self):
        return True
    
    def fight(self, opponent):
        return ATTACK_SCRATCH # ATTACK_SCRATCH is set to scratch
    
    def get_color(self):
        return "red" # sets the color of the animal to red
  
    def get_move(self):
        if self.walk_south == True: # If ant travels between south and east it comes from ant class it set with walk_south value of True 
            if self.alternate == 0:
                self.alternate = 1 # When it's set to one next time, it will travel east
                return DIRECTION_SOUTH
            else: 
                self.alternate = 0 # when it's put back to 0 it can travel south next time
                return DIRECTION_EAST
        else: # if walk_south is not true, it will go back and forward from north and south
            if self.alternate == 0:
                self.alternate = 1 # when it's put back to 1 it can travel west next time
                return DIRECTION_NORTH
            else:
                self.alternate = 0 # when it's put back to 0 it can travel north next time
                return DIRECTION_WEST
                
    
    def __str__(self): 
        return "%" #shape of ant

