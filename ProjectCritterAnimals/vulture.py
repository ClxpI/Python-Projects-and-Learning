# This class represents a Vulture type of Critter
# It 
# it is represented by a Black ("^" or "<" or ">" or "V")

from critter import *

class Vulture (Critter):
    def __init__(self,):
        super(Vulture, self).__init__()
        self.north = 0 # north is set to zero which is utilised to change directions
        self.east = 0 # east is set to zero which is utilised to change directions
        self.south = 0 # south is set to zero which is utilised to change directions
        self.west = 0 # west is set to zero which is utilised to change directions
        self.lastmove = 0 # lastmove is set to zero which is utilised to change directions and define the shape of vulture
        self.hungry = 1

    def eat(self):
        if self.hungry == 1: # if self.hungry is equal to 1 then it will eat 
            return True
        elif self.hungry != 1: # if self.hungry is not equal to 1 then it won't eat
            return False
        else:
            if opponent.__str__() == "%": # if the opponent is %, vulture will eat even if it's not hungry
                return True
    
    def get_color(self):
        return "Black" # sets color of vulture to black
          
    def fight(self, opponent):
        if opponent.__str__() == "%": # if the opponent is % it will roar otherwise it will pounce
            return ATTACK_ROAR # ATTACK_ROAR is set to roar
        else:
            return ATTACK_POUNCE # ATTACK_POUNCE is set to pounce

    def get_move(self):
        if self.north < 3: # if self.north is smaller than 3 then it will increase self.north value by 1 and set lastmove value to "north"
            self.north += 1
            self.lastmove = "north"
            return DIRECTION_NORTH # vulture will move north
        elif self.north == 3: # if self.north is equal to 3 then it will increase self.north and self.east value by 1 and set lastmove value to "east"
            self.north += 1
            self.east += 1
            self.lastmove = "east"
            return DIRECTION_EAST # vulture will move east
        elif self.east < 3: # if self.east is smaller than 3 then it will increase self.east value by 1 and set lastmove value to "east"
            self.east += 1
            self.lastmove = "east"
            return DIRECTION_EAST # vulture will move east
        elif self.east == 3: # if self.east is equal to 3 then it will increase self.east and self.south value by 1 and set lastmove value to "south"
            self.east += 1
            self.south += 1
            self.lastmove = "south"
            return DIRECTION_SOUTH # vulture will move south
        elif self.south < 3: # if self.south is smaller than 3 then it will increase self.south value by 1 and set lastmove value to "south"
            self.south += 1
            self.lastmove = "south"
            return DIRECTION_SOUTH # vulture will move south
        elif self.south == 3: # if self.south is equal to 3 then it will increase self.south and self.west value by 1 and set lastmove value to "west"
            self.south += 1
            self.west += 1
            self.lastmove = "west"
            return DIRECTION_WEST # vulture will move west
        else: # changes value of self.west by adding 1 and sets lastmove value to "west"
            self.west += 1
            self.lastmove = "west"
            return DIRECTION_WEST # vulture will move west

    # changes shape of vulture depending on the value of lastmove
    def __str__(self):
          if self.lastmove == "north":
              return "^" 
          elif self.lastmove == "east":
              return">"  
          elif self.lastmove == "south":
              return"V"  
          elif self.lastmove == "west": 
              return"<"  
          else:
              return "^" 
