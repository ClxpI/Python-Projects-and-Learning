def setup():
    size(200, 200)
    background(255)
    smooth()
    line(0, 0, 200, 0)
    line(0, 0, 0, 200)
    
    pushMatrix()
    fill(255, 0, 0) # Set the fill color to red for the first square.
    rotate(radians(30)) # Rotate the coordinate system by 30 degrees.
    translate(70, 70) # Move the origin to position (70, 70) for drawing.
    scale(2.0) # Scale the size of the shapes by a factor of 2.
    rect(0, 0, 20, 20) # Draw a red square at the new origin.
    popMatrix()

    pushMatrix() #allows transformtaion
    fill(255) # Set the fill color to white for the second square.
    translate(70, 70) # Move the origin to position (70, 70) again.
    rotate(radians(30)) # Rotate the coordinate system by 30 degrees.
    scale(2.0) # Scale the size of the shapes by a factor of 2.
    rect(0, 0, 20, 20) # Draw a white square at the transformed origin.
    popMatrix()
