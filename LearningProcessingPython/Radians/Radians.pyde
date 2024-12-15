size(700,500)
background('#4146C9') #background blue color

stroke('#FFFFFF') #line color
strokeWeight(3) #line width

fill('#4DCE34')
arc(width/2, height/2, 400, 400, 4.85, 5.4, PIE) #Green radiant


fill('#11BCF7')
arc(width/2, height/2, 300, 300, 4.85, 5.75, PIE) #Blue radiant
arc(width/2, height/2, 300, 300, 5.75, 2*PI, PIE) #Blue radiant next to previous one

fill('#FF0000')
arc(width/2, height/2, 200, 200, 0, PI, PIE) #Red radiant

fill('#FAA9F2')
arc(width/2, height/2, 300, 300, PI, 4.85, PIE) #Rose radiant
arc(width/2, height/2, 300, 300, PI, 4, PIE) #Rose radiant

fill('#FF39BA')
arc(width/2, height/2, 200, 200, PI, 4.85, PIE) #Rose(dark tone) radiant

fill('#9515AF')
arc(width/2, height/2, 200, 200, 4.85, 2*PI, PIE) #Purple Radiant

fill('#4146C9')
arc(width/2, height/2, 100, 100, 0, 2*PI) #Full circle, Same colour as background
