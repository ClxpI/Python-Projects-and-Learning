y=1

def setup():
    print(y) #prints initial value of y
    size(500, 500)
    noFill()
    stroke('#FFFFFF')
    strokeWeight(3)
def draw(): # runs the code within the method draw infinitely
    global y #uses the global vaiable y
    y += 1 #adds 1 each time the code runs again
    print(y) 
    background ('#004477')
    circle(height/2, y, 50) #draws a circle with the updated y value to animate it
