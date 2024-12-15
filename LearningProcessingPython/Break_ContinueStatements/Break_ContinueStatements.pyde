size(800,800)
background('#3525CB')

stroke('#FF0000') #line color
strokeWeight(11) #line width
line(499,0,509,800)
line(599,0,609,800)

noStroke() 
strokeWeight(1)

for i in range(20, width, 20): #loops until i = 20, draws a circle every 20th pixel on the x-AXIS
    fill('#0099FF')
    circle(i,75,10)


for i in range(20, width, 20): #loops until i = 20, draws a circle every 20th pixel on the x-AXIS
    if red(get(i, 225)) == 255: #when hitiing the red line it will skip the code and continue running loop wit i+1
        continue 
    fill('#00FF00') #changes the color to green
    circle(i, 225, 10)


for i in range(20, width, 20): #loops until i = 20, draws a circle every 20th pixel on the x-AXIS
    if red(get(i, 225)) == 255: #when hitiing the red line it will stop the code 
        break
    fill('#EDB518')
    circle(i,150,10)
