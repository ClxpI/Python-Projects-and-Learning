size(800,800)
image(loadImage('grid.png'),0,0)

stroke('#FFFFFF')
strokeWeight(3)
fill('#6633FF')

beginShape() #draws the coin circle
vertex(100,600)
bezierVertex(100,545,145,500,200,500)
bezierVertex(200,500,300,500,300,600)
bezierVertex(300,600,300,700,200,700)
bezierVertex(200,700,100,700,100,600)
beginContour() #removes the space inside de circle, creating a square hole
vertex(170,570)
vertex(170,630)
vertex(230,630)
vertex(230,570)
endContour()
endShape(CLOSE)
