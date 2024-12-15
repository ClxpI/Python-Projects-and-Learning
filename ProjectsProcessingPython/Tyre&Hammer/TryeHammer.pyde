def setup():
    size(800, 600)
    background('#FFFFFF')
    smooth()

def draw():
    noLoop()  # Ensures that the draw loop only runs once
    # First I will draw the Main wheel
    stroke(0) # This will set the line color to black
    strokeWeight(3) # This will set the line width to 3
    fill('#FF5100')# red color
    #This code will draw the red circle of the tyre, using multiple circles to create the 3d effect
    ellipse(370, 298, 150, 200)
    noStroke() #This will make the next circle to not have a line so they blend in together
    ellipse(376, 298, 150, 200)
    ellipse(380, 298, 150, 200)
    ellipse(384, 298, 150, 200)
    ellipse(386, 298, 150, 200)
    ellipse(390, 298, 150, 200)
    stroke(0) # this will set the line color to black
    line(362,198,403,199) #This lines will help to blend in the circles to give it the 3d effect 
    line(360,398,403,399)
    
    fill('#33C8F0') #light blue color
    #This will draw the blue circle of the tyre
    stroke(0)
    ellipse(400, 300, 150, 200)

    
    fill('#FFFFFF') #white color
    #This code will draw the white circle inside the tyre
    ellipse(389, 295, 50, 105)
    
    
    fill('#FF5100')# red color
    #This code will draw the inner circle lines
    beginShape() #left - bottom
    vertex(365,310)
    vertex(367,330)
    vertex(400,320)
    vertex(400,300)
    vertex(365,310)
    endShape()
    beginShape() #bottom
    vertex(395,318)
    vertex(400,350)
    vertex(423,348)
    vertex(418,310)
    vertex(395,318)
    endShape()
    beginShape() #right
    vertex(420,310)
    vertex(437,310)
    vertex(437,290)
    vertex(420,290)
    vertex(420,310)
    endShape()
    beginShape() #top
    vertex(410,290)
    vertex(420,246)
    vertex(400,237)
    vertex(390,290)
    vertex(410,290)
    endShape()
    beginShape() #top-left
    vertex(400,290)
    vertex(370,260)
    vertex(364,280)
    vertex(400,310)
    vertex(400,290)
    endShape()


    # This will draw the Wheel center
    fill('#F7A100') #orange wooden tone color
    ellipse(398, 297, 40, 45)
    ellipse(405, 300, 40, 45)
    fill('#33C8F0') #light blue color
    ellipse(405, 300, 15, 15)
    #This will draw the circle in the middle without any color to give the 3d effect of the wheel
    noFill()
    ellipse(400, 300, 75, 125)
    
    # This will draw the hammer
    fill('#F7A100') #orange wooden tone color
    beginShape() #Hammer handle
    curveVertex(550,410)
    curveVertex(550,410)
    curveVertex(580,390)
    curveVertex(520,240)
    curveVertex(500,240)
    curveVertex(550,410)
    curveVertex(550,410)
    endShape()

    #draw hammer head here
    fill('#33C8F0')  # Light blue color for hammer head
    beginShape()
    curveVertex(584, 230) #CruveVertex to make curved edges
    curveVertex(584, 230) 
    curveVertex(565, 200)
    curveVertex(440, 230)
    curveVertex(450, 270)
    curveVertex(585, 230)  
    curveVertex(585, 230)  
    endShape()
    fill('#FA3559')  # Red-pink color for the front of the hammer head
    beginShape()
    curveVertex(432, 233)
    curveVertex(432, 233) 
    curveVertex(435, 270)
    curveVertex(460, 270)
    curveVertex(460, 235)
    curveVertex(435, 233)  
    curveVertex(435, 233)  
    endShape()
    #This will draw the hammer head lines for a 3d effect
    line(465, 233, 525, 218)
    line(530, 215, 540, 243)
    line(530, 215, 520, 207)
    line(533, 223, 574, 212)
    stroke(255) #for white lines
    line(525,260,575,390)
    line(520,260,543,320)
    stroke(0) #for black lines
    fill('#F7A100') #orange wooden tone color for hammer
    ellipse(500,215, 20,15)
    
