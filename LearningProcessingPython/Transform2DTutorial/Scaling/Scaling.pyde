def setup():
    size(200,200)
    background(255)
    
    stroke(128)
    rect(20, 20, 40, 40)
    
    stroke(0)
    pushMatrix() 
    translate(-40,-40) # origin of the coordinates set to (40, 40)
    scale(3.0) #change the size to 3x bigger
    rect(20, 20, 40, 40)
    popMatrix()
