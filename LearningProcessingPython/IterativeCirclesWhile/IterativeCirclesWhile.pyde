size(500, 500)
background('#00477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

i = 1
while i < 17: # we set the value to 17 so there is no broken circles using the while loop
    circle(width/2, height/2, i * 30)
    i = i + 1 #increases the value of i by one each time the while loop starts again
