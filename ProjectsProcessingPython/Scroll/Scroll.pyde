def setup():
    size(545, 552)
    background('#FCF9F0')  # Assuming a white background

def draw():
    noLoop()
    draw_rods_left()
    draw_scroll()
    draw_rods_right()
    draw_text()

def draw_scroll():
    fill('#F5EAAF')  # Off-white color for the scroll
    stroke('#F5EAAF')
    
    #Middle scroll
    rect(100, 100, 345, 200)
    stroke('#D6CC95')
    # Top scroll
    x=30
    y=50
    rect(100, 100, 345, 50)  # The top part of the scroll
    arc(100, 125, 50, 50, HALF_PI, PI + HALF_PI)  # Left rolled edge
    for i in range(10):
        ellipse(445, 125, x, y) 
        x -= 3
        y -= 3 

    # Bottom scroll
    w = 30
    z = 50
    rect(100, 275, 345, 50)  # The bottom part of the scroll
    arc(100, 300, 50, 50, HALF_PI, PI + HALF_PI)  # Left rolled edge
    for i in range(10):
        ellipse(445, 300, w, z) 
        w -= 3
        z -= 3 

def draw_rods_right():
    fill('#8B4513')  
    stroke('#8B4513')
    fill(139, 69, 19)  # Brown color for the rods
  
    # Top rod
    rect(450, 115, 30, 20)  # The central part of the rod
    ellipse(480, 125, 20, 20)  # Right end of the rod
  
    # Bottom rod
    rect(450, 295, 30, 20)
    ellipse(480, 305, 20, 20)  # Right end of the rod

    
def draw_rods_left():
    fill('#8B4513')  
    stroke('#8B4513')
  
    # Top rod
    rect(75, 115, 395, 20)  # The central part of the rod
    ellipse(75, 125, 20, 20)  # Left end of the rod

  
    # Bottom rod
    rect(75, 295, 395, 20)  # The central part of the rod
    ellipse(75, 305, 20, 20)  # Left end of the rod


def draw_text():
    fill(0)  # Black color for the text
    textSize(32)  # Size for the text
    # Create the font for the text. You can choose your preferred font here.
    text_font = createFont("Algerian", 32)
    textFont(text_font)
    textAlign(CENTER, CENTER)
    text("WHEELS", width / 2, 212.5)  # Positioning the text at the center of the scroll
