def setup():
    size(200, 200)
    background(255)
    smooth()
    drawRobot()

def drawRobot():
    noStroke()             # Disables drawing the stroke (outline) of shapes
    fill(38, 38, 200)      # Sets the fill color for shapes (blue)
    rect(20, 0, 38, 30)    # Draws the robot's head as a rectangle
    rect(14, 32, 50, 50)   # Draws the robot's body as a rectangle
    
    drawLeftArm()          # Calls function to draw the left arm
    drawRightArm()         # Calls function to draw the right arm
    
    rect(22, 84, 16, 50)   # Draws the left leg
    rect(40, 84, 16, 50)   # Draws the right leg
    
    fill(222, 222, 249)    # Changes fill color to light blue
    ellipse(30, 12, 12, 12)# Draws left eye as an ellipse
    ellipse(47, 12, 12, 12)# Draws right eye as an ellipse

def drawLeftArm():
    pushMatrix()
    translate(12, 32)
    rect(-12, 0, 12, 37)
    popMatrix()

def drawRightArm():
    pushMatrix()
    translate(66, 32)
    rect(0, 0, 12, 37)
    popMatrix()
    
def drawLeftArm():
    pushMatrix()
    translate(12, 32)      # Moves the origin to the left arm's shoulder joint
    rotate(radians(135))   # Rotates the coordinate system by 135 degrees
    rect(-12, 0, 12, 37)   # Draws the left arm as a rectangle
    popMatrix()

def drawRightArm():
    pushMatrix()
    translate(66, 32)      # Moves the origin to the right arm's shoulder joint
    rotate(radians(-45))   # Rotates the coordinate system by -45 degrees
    rect(0, 0, 12, 37)     # Draws the right arm as a rectangle
    popMatrix()

armAngle = 0
angleChange = 5
ANGLE_LIMIT = 135

def setup():
  size(200, 200)
  smooth()
  frameRate(30)

def draw():
    global armAngle, angleChange, ANGLE_LIMIT  # Global variables for arm movement
    print(armAngle)
    background(255)
    pushMatrix()          # Saves the current transformation matrix
    translate(50, 50)     # Moves the origin to help keep arms visible during rotation
    drawRobot()        

    armAngle += angleChange  # Increments the arm angle by the change amount

    # Checks if the arm angle exceeds the set limits
    if armAngle > ANGLE_LIMIT or armAngle < 0:
        angleChange = -angleChange  # Reverses the direction of the arm movement
        armAngle += angleChange     # Applies the reversed direction immediately
    popMatrix()



def drawLeftArm():
    global armAngle
    pushMatrix()
    translate(12, 32)
    rotate(radians(armAngle))  # Uses armAngle to rotate the left arm
    rect(-12, 0, 12, 37)
    popMatrix()

def drawRightArm():
    global armAngle
    pushMatrix()
    translate(66, 32)
    rotate(radians(-armAngle)) # Uses armAngle to rotate the right arm
    rect(0, 0, 12, 37)
    popMatrix()
