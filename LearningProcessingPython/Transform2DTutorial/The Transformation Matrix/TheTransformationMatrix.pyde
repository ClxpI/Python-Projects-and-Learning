def setup():
  size(400, 300)
  background(255)
  for i in xrange(10,350,70): 
    house(i, 50)
    
def house(x, y):
  pushMatrix() 
  translate(x, y) # origin of the coordinates set to (x, y)
  triangle(30, 0, 0, 30, 60, 30) #ceiling
  rect(0, 30, 60, 60) #wall
  rect(24, 60, 20, 30) #door
  popMatrix()
