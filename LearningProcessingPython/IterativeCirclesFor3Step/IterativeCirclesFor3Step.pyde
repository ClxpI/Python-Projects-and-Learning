size(500, 500)
background('#00477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)


for i in range (1,17, +2): # we set the value to 17 so there is no broken circles
    print(i)
    circle(width/2, height/2, 30 * i)
    