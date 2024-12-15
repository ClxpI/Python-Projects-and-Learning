def setup():
    size(200, 200)
    background(255)
    smooth()
    fill(192)
    noStroke()
    rect(40, 40, 40, 40)
    
    pushMatrix()
    translate(40, 40) # origin of the coordinates set to (40, 40)
    rotate(radians(45)) # Rotate by 45 degrees.
    fill(0)
    rect(0, 0, 40, 40)
    popMatrix()
