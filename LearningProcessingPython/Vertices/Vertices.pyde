size(800,800)
grid = loadImage('grid.png')
image(grid,0,0)

fill('#6633FF')
stroke('#FFFFFF')
strokeWeight(3)

beginShape(POINTS) # begins recording vertice for a shape
vertex(100,100)
vertex(200,100)
vertex(200,200)
vertex(100,200)
endShape(POINTS) 

beginShape()
vertex(400,200)
bezierVertex(300,300,500,500,400,600) #draws a curve
endShape()
