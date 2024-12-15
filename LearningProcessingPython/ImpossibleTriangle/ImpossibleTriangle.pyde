#This code draws an imposible triangle, which resembles the drawing 'Impossible cube' by Escher "Escher Challenge"
size(800,800)

background('#FFFFFF')
beginShape() #draws the white side of the triangle, a rotated and tilted L shape figure
vertex(360,320)
vertex(400,320)
vertex(550,510)
vertex(300,510)
vertex(320,480)
vertex(480,480)
vertex(380,350)
endShape()

fill('#000000')
beginShape()  #draws the black side of the triangle, a rotated and tilted L shape figure
vertex(550,510)
vertex(520,540)
vertex(225,540)
vertex(360,380)
vertex(385,410)
vertex(300,510)
vertex(550,510)
endShape()

fill('#A7A7A7')  #draws the gray side of the triangle, a rotated and tilted L shape figure
beginShape()
vertex(225,540)
vertex(360,380)
vertex(430,480)
vertex(480,480)
vertex(360,320)
vertex(200,510)
vertex(225,540)
endShape()
