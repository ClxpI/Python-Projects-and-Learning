def setup():
    size(800, 600)
    background('#B76212')
    noLoop()

def draw(): #calls methods different times to repeat drawings with different coordinates and sizes
    ceiling()
    back_wall()
    draw_floor()
    draw_cabinet(100, 100, 190, 300)
    draw_3d_sides(100, 100, 190, 300)
    fill_cabinet_with_books(100, 100, 190, 300, 13, 15)
    strokeWeight(1)
    stroke('#AD6338')
    fill('#892E00')
    rect(100,230,190,20)
    draw_cabinet(80, 70, 150, 400)
    draw_3d_sides(80, 70, 150, 400)
    fill_cabinet_with_books(80, 70, 150, 400, 13, 15)
    strokeWeight(1)
    stroke('#AD6338')
    fill('#892E00')
    rect(80,240,150,30)
    draw_cabinet(60, 30, 110, 500)
    draw_3d_sides(60, 30, 110, 500)
    fill_cabinet_with_books(60, 50, 110, 500, 13, 10)
    strokeWeight(1)
    stroke('#AD6338')
    fill('#892E00')
    rect(60,260,110,40)
    draw_cabinet(-150, 0, 250, 600)
    draw_3d_sides(-150, 0, 250, 600)
    fill_cabinet_with_books(-150, 0, 250, 600, 13, 15)
    strokeWeight(1)
    stroke('#AD6338')
    fill('#892E00')
    rect(-150,290,250,50)
    draw_cabinet(500, 100, 190, 300)
    draw_3d_sides(500, 100, 190, 300)
    fill_cabinet_with_books(500, 100, 190, 300, 13, 15)
    strokeWeight(1)
    stroke('#AD6338')
    fill('#892E00')
    rect(500,230,190,20)
    draw_cabinet(555, 70, 150, 400)
    draw_3d_sides(555, 70, 150, 400)
    fill_cabinet_with_books(555, 70, 150, 400, 13, 15)
    strokeWeight(1)
    stroke('#AD6338')
    fill('#892E00')
    rect(555,240,150,30)
    draw_cabinet(620, 30, 110, 500)
    draw_3d_sides(620, 30, 110, 500)
    fill_cabinet_with_books(620, 50, 110, 500, 13, 10)
    strokeWeight(1)
    stroke('#AD6338')
    fill('#892E00')
    rect(620,260,110,40)
    draw_cabinet(685, 0, 250, 600)
    draw_3d_sides(685, 0, 250, 600)
    fill_cabinet_with_books(685, 0, 250, 600, 13, 15)
    strokeWeight(1)
    stroke('#AD6338')
    fill('#892E00')
    rect(685,290,250,50)

def back_wall():
    fill('#A57323')
    noStroke()
    beginShape()#back wall 
    vertex(180,45)
    vertex(300,395)
    vertex(500,395)
    vertex(620,45)
    bezierVertex(480,55,360,55,180,45)
    endShape()
    fill('#FFFFFF') #top window
    beginShape()
    vertex(190,85)
    vertex(190,55)
    bezierVertex(250,70,530,70,590,55)
    vertex(590,85)
    bezierVertex(480,100,250,100,190,85)
    endShape()
    x = 180
    for i in range (15): #top window borders
        stroke('#A57323')
        strokeWeight(3)
        line(x, 55, x, 100)
        x = x + 30
    noStroke()
    fill('#714B2E') #wood color
    beginShape() #back wall wood decoration
    rect(320,150,150,245) 
    vertex(320,150)
    bezierVertex(320,130,340,120,395,120)
    vertex(395,120)
    bezierVertex(425,120,470,130,470,150)
    endShape()
    stroke('#672F04')
    strokeWeight(1)
    
    col = 327
    row = 240
    for i in range(8): #details back wall
        line(col, row, col,row+153)
        col += 19
    
    
    
    fill('#C9EDFF')
    rect(340,240,90,70) #window
 

def ceiling():
    col = -30
    row = 0
    for i in range(1, 27): #ceiling details, rombo shapes
        stroke('#9D3A13')
        strokeWeight(6)
        line(col, row, col+100, row+50)
        line(col, row, col-100, row+50)
        col += 100
        if i == 16:
            row += 50
            col =- 30
    
def draw_floor():
    col = 200
    row = 400
    for i in range(1, 50): #draws details randomly on floor everytime the code runs
        line(col, row, col+50,row)
        line(col, row+50, col+50, row+50) 
        col += random(30,120)
        if i % 11== 0:
            row += random(50)
            col = 150
    fill('#C9EDFF')
    
    
    
    
def draw_cabinet(x, y, w, h):
    strokeWeight(2)
    stroke('#AD6338')
    fill(150, 75, 0)
    rect(x, y, w, h)
    # Draw cabinet doors
    fill(100, 50, 0)
    rect(x, y, w/2, h)
    line(x + w/2, y, x + w/2, y + h)


def fill_cabinet_with_books(x, y, w, h, num_shelves, num_books_per_shelf):
    noStroke()
    shelf_gap = h / (num_shelves + 1)
    book_width = w / (num_books_per_shelf * 2)
    book_height = shelf_gap * 0.8
    for i in range(1, num_shelves + 1):
        shelf_y = y + i * shelf_gap
        for j in range(num_books_per_shelf):
            book_x = x + (2*j + 1) * (w / (num_books_per_shelf * 2))
            fill(random(255), random(255), random(255))
            rect(book_x, shelf_y - book_height, book_width, book_height)

def draw_3d_sides(x, y, w, h):
    side_width = 15
    fill('#892E00')
    beginShape()
    vertex(x, y)
    vertex(x - side_width, y - side_width/2)
    vertex(x - side_width, y + h - side_width/2)
    vertex(x, y + h)
    endShape(CLOSE)
    
    beginShape()
    vertex(x + w, y)
    vertex(x + w + side_width, y - side_width/2)
    vertex(x + w + side_width, y + h - side_width/2)
    vertex(x + w, y + h)
    endShape(CLOSE)
    
    # Draw top side
    beginShape()
    vertex(x, y)
    vertex(x + w, y)
    vertex(x + w + side_width, y - side_width/2)
    vertex(x - side_width, y - side_width/2)
    endShape(CLOSE)
