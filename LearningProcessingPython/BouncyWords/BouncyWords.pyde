y = 100
yspeed = 2
x = 100
xspeed = 2

def setup():
    size(800, 600)
    fill('#0099FF')
    textSize(70) # Defines text size
    
def draw():
    global y, yspeed, x, xspeed # imports gloabal variables
    background ('#000000')
    y += yspeed #changes position based on speed
    x += xspeed
    text('CMU507', x, y) #sets text and text position
    if y <0+50 or y > height: #limits the text to stay within the height of the window, so it bounces when hitting an edge
        yspeed +=-1
    if x < 8 or x > width - textWidth('CMU507'): #limits the width, bounces when hitting sides of the window
        xspeed +=-1
