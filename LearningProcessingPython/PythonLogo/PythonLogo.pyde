size(800,800) #window size
image(loadImage('grid.png'),0,0) #grid image
image(loadImage('logo_paths.png'),0,0) #image logo path

#set line width and color for lines
noFill()
stroke('#FFFFFF')
strokeWeight(6)

beginShape() #top-left curve
vertex(265,177)
bezierVertex(275,20,400,30,500,30)
endShape()

beginShape() #top-right curve
vertex(735,177)
bezierVertex(725,25,600,30,500,30)
endShape()

beginShape() #middle-left curve
vertex(173,267)
bezierVertex(10,293,37,400,30,500)
endShape()

beginShape() #bottom-left curve
vertex(30,500)
bezierVertex(30,600,25,720,173,735)
endShape()

beginShape() #middle curve
vertex(236,630)
bezierVertex(240,540,300,490,378,487)
endShape()

beginShape() #bottom-right curve
vertex(622,487)
bezierVertex(660,490,715,475,735,373)
endShape()

noFill()
circle(368, 143, 80)

#left side lines
line(265,177,265,237)
line(265,237,497,237)
line(497,237,497,267)
line(497,267,173,267)

#right side line
line(735,177,735,373)

#bottom lines
line(378,487,622,487)
line(236,630,236,735)
line(173,735,236,735)
