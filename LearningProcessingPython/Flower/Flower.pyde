size(800,800)
flower = loadImage('background.png') #imports background image
flower.resize(800, 800) #resizes image to fit
image(flower, 0, 0) #sets image as background

fill('#02A200') #green color
noStroke() # no lines
rect(353,340,20,460) #floor stick
ellipse(370, 550, 30, 30) #leaf
ellipse(355, 620, 30, 30) #leaf
stroke(2) #line width
fill('#FF9100') #orange color
circle(270, 250, 180) # draws 4 circles to make the flower
circle(450, 250, 180)
circle(270, 430, 180)
circle(450, 430, 180)
fill('#FFF300') #yellow color
circle(360, 340, 180) #flower center circle
