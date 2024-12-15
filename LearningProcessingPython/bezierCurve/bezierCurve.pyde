size(800,500)
grid = loadImage('grid.png')
image(grid, 0, 0)

strokeWeight(2) # line width
stroke('#FF99FF') #line color
cp1x = 250
cp1y = 250
cp2x = 250
cp2y = 250
bezier(400,100,cp1x,cp1y,cp2x,cp2y,100,400) # draws line
