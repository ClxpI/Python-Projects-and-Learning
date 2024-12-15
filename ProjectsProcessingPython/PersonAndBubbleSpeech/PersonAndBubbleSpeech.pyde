def setup():
    size(800, 600)
    background(255)

def draw():
    noLoop()
    draw_head()
    draw_body()
    draw_speech_bubble()

def draw_head():
    fill(0) #black color for the eyes
    ellipse(400,220,20,40) #left eye
    ellipse(460,220,20,40) #right eye 
    noFill()
    beginShape() #Draws the perimeter of the head
    vertex(400,100)
    bezierVertex(430,80,480,90,520,120)
    vertex(525,115)
    vertex(527,120)
    vertex(535,115)
    vertex(536,123)
    bezierVertex(545,135,560,160,580,180)
    vertex(570,180)
    vertex(560,240)
    bezierVertex(560,260,540,280,525,280)
    vertex(520,290)
    vertex(500,310)
    bezierVertex(470,320,410,340,370,320)
    vertex(360,260)
    vertex(355,250)
    vertex(352,200)
    vertex(340,210)
    vertex(342,170)
    vertex(335,160)
    vertex(343,160)
    vertex(340,150)
    bezierVertex(350,130,370,110,400,100)
    endShape()
    #Head detailing
    beginShape() #This draws the hairline
    vertex(352,200)
    bezierVertex(360,180,370,160,390,140)
    vertex(500,150)
    bezierVertex(490,160,510,180,530,190)
    vertex(530,240)
    bezierVertex(540,200,550,210,562,230)
    endShape()
    #nose
    line(420,220,400,260)
    line(400,260,430,260)
    line(430,260,430,255)
    #mouth
    line(405,285,440,285)
    #eyebrows
    beginShape() #left eyebrow
    vertex(360,195)
    vertex(410,200)
    vertex(415,190)
    bezierVertex(410,180,390,185,360,195)
    endShape()
    beginShape() #right eyebrow
    vertex(490,195)
    vertex(440,200)
    vertex(435,190)
    bezierVertex(440,180,470,185,490,195)
    endShape()
    #facial details
    line(360,260,370,265)
    line(380,275,383,315)
    line(440,255,465,300)
    line(470,255,475,300)
    line(490,280,490,310)
    line(480,255,495,245)
    line(400,165,420,165)
    line(430,165,450,165)
    line(395,175,415,175)
    line(425,175,445,175)

def draw_body():
    #This draws the shirt
    line(500,310,500,320)
    line(500,320,515,340)
    line(515,340,570,380)
    line(570,380,590,530)
    line(530,420,520,530)
    line(515,340,460,400)
    line(460,400,445,365)
    line(445,365,430,375)
    line(500,320,425,360)
    line(425,360,420,370)
    line(420,370,400,390)
    line(400,390,390,530)
    line(420,370,405,330)
    line(405,330,375,400)
    line(375,400,400,360)
    line(400,360,418,373)
    line(405,330,340,380)
    line(340,380,320,530)
    line(345,390,345,530)
    beginShape()#shirt pocket
    vertex(440,450)
    vertex(500,450)
    vertex(500,510)
    vertex(470,530)
    vertex(440,510)
    endShape(CLOSE)    
    #Buttons
    circle(410,395,10)
    fill(0)
    circle(410,440,5)
    circle(410,480,5)



def draw_speech_bubble():
    # Speech bubble as an ellipse for this example
    fill(255)
    stroke(0)
    ellipse(230, 200, 150, 150)
    # Text in the speech bubble
    fill(0)
    textSize(16)
    textAlign(CENTER, CENTER)
    text("IT", 230, 180)
    text("DIDN'T", 230, 200)
    text("WORK!", 230, 220)
