size(600, 600)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

col =0
row =0

for i in range(1, 145): #draws a pattern of arcs 144 times
    if i % 12 == 0: # every multiple of 12 col is set to 0 and row is equal to row plus 50.
        row += 50
        col = 0
    arc(col, row, 50, 50, 0, PI/2)
    arc(col+50, row+50, 50, 50, PI, PI*1.5)
    col += 50
