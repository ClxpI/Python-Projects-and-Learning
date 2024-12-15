size(800,800)
grid = loadImage('grid.png') #imports image
image(grid,0,0) #sets image as background

fill('#6633FF') #purple color
stroke('#FFFFFF') #white color line
strokeWeight(3) #line width

fill('#FF0000') #red color
beginShape() #left side of heart
vertex(600,400) 
bezierVertex(420,320,550,150,600,280) #draws a curve
endShape()

beginShape() #right side of heart
vertex(600,400)
bezierVertex(780,320,650,150,600,280) #draws a curve
endShape()
