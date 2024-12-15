def setup(): 
    size(500, 500)
    background('#004477') 
    noFill()
    stroke('#FFFFFF')
    strokeWeight(3)
    frameRate(12.5) #sets a framerate to adjust animation speed

def draw(): # draws the loading animation, same as Microsoft loading screen 
    background('#004477')
    if frameCount % 8 != 2: #when framcount MOD 8 is not equal to 2 it will print a circle
        print(frameCount)
        circle(420, 250, 80)
    hide = frameCount % 8
    if hide != 0: #hides the circle until framecounts MOD 8 is equal to the value set, ie: 0
        circle(250,80,80)
    if hide != 1:
        circle(365,130,80)
    if hide != 3:
        circle(365,360,80)
    if hide != 4:
        circle(250,420,80)
    if hide != 5:
        circle(150,360,80)
    if hide != 6:
        circle(100,250,80)
    if hide != 7:
        circle(150,130,80)



    
