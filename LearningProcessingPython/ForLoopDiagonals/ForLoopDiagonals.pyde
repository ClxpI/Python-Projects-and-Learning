size(800, 300)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

# left pattern (left)
for i in range(12):
    print(i)
    line(55, 100+i*13, 210, 50+i*13)

# left pattern (right)
for x in range(8):
    print(x)
    x = x*2
    line(300, x*x+40, 430, 50+x*x+40)

# right pattern (left)
for y in range(7):
    print(y)
    line(600, 100+y*30, 665, 50+y*30)

# right pattern (right)
for y in range(6):
    print(y)
    line(665, 65+y*30, 730, 115+y*30)

    
