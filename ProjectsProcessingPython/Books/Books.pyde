def setup():
    size(800, 600)
    background(250)

def draw_book(): #draw books
    y = 150
    fill('#582D34')
    stroke(('#4B262D'))
    for i in range (10): #bottom book
        beginShape()
        vertex(280, y+20)  
        vertex(450, y+200)  
        vertex(550, y+140)
        vertex(400, y-30)  
        endShape(CLOSE)  
        y -= 2
    
    stroke('#222643')
    fill('#545879')
    for i in range (10): #top book
        beginShape()
        vertex(300, y)  
        vertex(430, y+180)  
        vertex(550, y+130)
        vertex(430, y-20)  
        endShape(CLOSE)  
        y -=2

    stroke('#FFFFFF')
    fill('#FFFFFF')
    beginShape() #Top book pages
    vertex(440,290)
    vertex(550,245)
    vertex(550, 257)
    vertex(440,300)
    endShape()
    beginShape() #bottom book pages
    vertex(455,337)
    vertex(550,277)
    vertex(550,287)
    vertex(455,347)
    endShape()
    # Adding text on the book
    fill('#FFFFFF')  # Text color
    textSize(20)  # Text size
    textFont(createFont("Arial", 30))  # You can choose your font
    # Shear and position the text to simulate the perspective
    pushMatrix()
    translate(340, 140)  # Adjust translation to position text correctly
    shearX(PI / 6.0)  # Shear the text for fake perspective
    text("Statistics", 0, 0)  # The text to display
    popMatrix()
    
def draw_wood():
    fill('#CEA470')  # Dark Wood color for shadow
    noStroke()
    y = 100
    for i in range(10):  # Draws the same wood piece one on top of other creating a 3d effect
        beginShape()
        curveVertex(400, y)
        curveVertex(400, y)
        curveVertex(247, y + 150)
        curveVertex(390, y + 300)
        curveVertex(553, y + 150)
        curveVertex(400, y)
        curveVertex(400, y)
        endShape(CLOSE)
        y += 2
    fill('#DEB887')  # Light wood color
    stroke('#CEA470')  # Dark wood color to blend top with shadow
    beginShape()  # This draws the top wood
    curveVertex(400, 100)
    curveVertex(400, 100)
    curveVertex(250, 250)
    curveVertex(390, 400)
    curveVertex(550, 250)
    curveVertex(400, 100)
    curveVertex(400, 100)
    endShape(CLOSE)
    
def draw():
    noLoop()
    draw_wood()
    draw_book()
