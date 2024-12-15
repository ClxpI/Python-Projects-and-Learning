size(561,768)
art = loadImage('The_Arnolfini_portrait_(1434).jpg')
image (art,0,0,width,height)



    
def speechBubble(x, y, txt='Hello', type='speech'):
    noStroke()
    pushMatrix()
    translate(x, y)
    # tail
    if type == 'speech':
        fill('#FFFFFF')
        beginShape()
        vertex(0, 0)
        # tip
        vertex(15, -40)
        vertex(35, -40)
        endShape (CLOSE)
    elif type == 'thought':
        fill('#FFFFFF')
        circle(0, 0, 8)
        circle(10, -20, 20)
    
    # bubble
    textSize(15)
    by = -85
    bw = textWidth(txt)
    pad = 20
    rect(0, by, bw+pad*2, 45, 10)
    fill('#000000')
    textAlign(LEFT, CENTER)
    text(txt, pad, by+pad)
    popMatrix()
    
def shout(txt):
    return txt.upper() + '!!!'

speechBubble(190, 150, shout('Check out my hat'))
speechBubble(315, 650, 'Woof')
speechBubble(txt='Woof', x=315, y=650)
speechBubble(445, 125, 'Wow', 'thought')
