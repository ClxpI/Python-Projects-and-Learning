def setup():
    size(800, 600)
    background('#F2EADF')
    noLoop()

def draw():
    shadow(-300,390,700,20)
    stroke(0)
    # Starting position for the scrolls
    start_x = 230
    scrolls_spacing = 40  # Space between scrolls
    num_scrolls = 7  # Number of scrolls

    draw_table(150, 300, 400, 20)

    # Draw the scrolls using a loop
    for i in range(num_scrolls):
        draw_scrolls(start_x + i * scrolls_spacing, 200)

    draw_table(150, 300, 400, 20)

def draw_scrolls(x, y):
    fill('#E8DCBE')
    ellipse(x, y-5, 18, 8)
    ellipse(x, y, 22, 10)  # Top circle of scrolls
    rect(x - 10, y, 20, 100)  # Main body of scrolls
    ellipse(x, y + 97, 22, 10)
    ellipse(x, y + 100, 15, 8)  # Bottom circle of the scrolls

def draw_table(x, y, width, height):
    fill('#BF8334')  # Darker brown for the table
    rect(x, y, width, height)  # Top surface of the table
    # Draw the table's legs
    rect(x + 10, y + height, 15, 100)  # Left leg
    rect(x + width - 25, y + height, 15, 100)  # Right leg
    rect(x + 40, (y-20) + height, 15, 100)  # Left-Middle leg
    rect(x + width - 55, (y-20) + height, 15, 100)  # Right-Middle leg
    rect(x + 25, y+ height, x+200, 30)
    rect(x + 25, y+ height, x+200, 25)
    rect(x+25,y +height, 75, 25)
    rect(x+100,y +height, 75, 25)
    rect(x+175,y +height, 75, 25)
    rect(x+250,y +height, 75, 25)
    circle(x+140, y+ (height+13),8)
    circle(x+290, y+ (height+13),8)

def shadow(x,y,width,height): # Draw shadows
    noStroke()
    for i in range(5): # Desk shadow
        fill(0, 0, 0, 30)  # Semi-transparent black
        ellipse(x + width / 2, y + height, width - i * 10, height - i * 5) 
    # Desk legs shadows
    ellipse(200,400,630,5)
    ellipse(200,420,660,5)
        
