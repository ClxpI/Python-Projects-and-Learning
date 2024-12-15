# set values to variables
y = 100
yspeed = 10
x = 100
xspeed = 10
w = 200
wspeed = 2
z = 200
zspeed = 2
radius = 40 

def setup():
    size(800, 600)

def draw():
    #import global variables so they can be modified
    global y, yspeed, x, xspeed, w, wspeed, z, zspeed
    background ('#000000')
    y += yspeed
    x += xspeed
    w += wspeed
    z += zspeed
    # Draw circles
    fill('#0099FF')
    circle(x, y, 2*radius)
    fill('#FC0000')
    circle(w, z, 2*radius)
    # Check collision with edges and updates the speeds
    if y < radius or y > height - radius:
        yspeed *= -1
    if x < radius or x > width - radius:
        xspeed *= -1
    if z < radius or z > height - radius:
        zspeed *= -1
    if w < radius or w > width - radius:
        wspeed *= -1
    
    # Check collision between circles and swaps speed between balls when they collide
    if dist(x, y, w, z) < 2*radius:
        xspeed, wspeed = wspeed, xspeed
        yspeed, zspeed = zspeed, yspeed
