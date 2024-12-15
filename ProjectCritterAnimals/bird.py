# This class represents a Bird type of Critter
# It stays still, doesn't eat and roars if opponet looks like Ant otherwise pounces
# it is represented by a blue >

from critter import *

class Bird (Critter):
    def __init__(self):
        super(Bird, self).__init__()
        self.last = 0 # attribute is zero when set which is utilised to change directions
        self.north = 0 # attribute is zero when set which is utilised to change directions
        self.east = 0 # attribute is zero when set which is utilised to change directions
        self.south = 0 # attribute is zero when set which is utilised to change directions
        self.west = 0 # attribute is zero when set which is utilised to change directions

    def eat(self):
        return False #bird is never hungry

    def fight(self, opponent):
        if opponent.__str__() == "%":
            return ATTACK_ROAR # ATTACK_ROAR is set to Roar
        else:
            return ATTACK_POUNCE # ATTACK_POUNCE is set to Pounce
    
    def get_color(self):
        return "blue" #sets color of Bird to blue
  
    def get_move(self):
        if self.north < 3:
            self.north = self.north + 1
            self.last = "North"
            return DIRECTION_NORTH # When it's set to 3 next time, it will travel north
        elif self.north == 3:
            self.east = self.east + 1
            self.north = self.north + 1
            self.last = "East"
            return DIRECTION_EAST # When it's set to 3 next time, it will travel east
        elif self.east < 3:
            self.east = self.east + 1
            self.last = "East"
            return DIRECTION_EAST # When it's set to 3 next time, it will travel east
        elif self.east == 3:
            self.south = self.south + 1
            self.east = self.east + 1
            self.last = "South" 
            return DIRECTION_SOUTH # When it's set to 3 next time, it will travel south
        elif self.south < 3:
            self.south = self.south + 1
            self.last = "South"
            return DIRECTION_SOUTH # When it's set to 3 next time, it will travel south
        elif self.south == 3:
            self.west = self.west + 1
            self.south = self.south + 1
            self.last = "West"
            return DIRECTION_WEST # When it's set to 3 next time, it will travel west
        else:
            self.north = 1
            self.east = 0
            self.south = 0
            self.west = 0
            self.last = "North"
            return DIRECTION_NORTH # When it's set to 3 next time, it will travel north

    #defines the shape of bird depending on the direction it moves                                                                                                                                                  
    def __str__(self):
        if self.last == "North": # if the bird's last move was north or it has not moved;
            return "^"
        elif self.last == "East": # if the bird's last move was east;
            return">"
        elif self.last == "South": # if the bird's last move was south;
            return"V"
        elif self.last == "West": # if the bird's last move was west;
            return"<"
        else:
            return"^" # if the bird doesn't move its shape will be "^" 
   

