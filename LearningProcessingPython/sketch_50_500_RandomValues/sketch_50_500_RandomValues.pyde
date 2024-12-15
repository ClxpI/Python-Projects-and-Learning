size(500, 500)
background('#004477')

stroke('#FFFFFF')
strokeWeight(9)

for i in range(50): #loops the code 50 times
    point(random(width),height/2) #draws a point in the center of the y axis to a random x position

for i in range(500): #loops the code 500 times
    point(random(width),random(height))  #draws a point randomly anywhere within the height and width
