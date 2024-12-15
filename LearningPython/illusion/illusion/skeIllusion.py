'''
    Author: Mohammad Ismail Ashiq Aslam
    Task: illusion
    Part: B - Cafewall
    
'''
import random
from drawingPanel import *          # import drawingPanel


# Function to draw a square
def drawSquare(canvas,x1,y1,x2,y2, fillColour):
    canvas.create_rectangle(x1,y1,x2,y2,fill = fillColour)
       


# Function to draw a row
def drawRow(canvas, startX, startY, pairs, size):
    # Draw individual squares in the row
    for box in range(pairs * 2):
        # Determine the colour to fill an individual box with
        if (box % 2) == 0:
           fillColor = "Black"
        else:
           fillColor = "White"
        # Draw square
        drawSquare(canvas, startX, startY, startX + size, startY + size, fillColor)
        # Calculate new X co-ordinate (startX + size)
        startX = startX + size



# Function to draw a grid which consists of a set of rows
def drawGrid(canvas, startX, startY, pairs, size, offset, rows):
    # Store the orginal value of the X co-ordinate
    originalStartX = startX
    # Draw individual rows in the grid
    for row in range (rows):
       drawRow(canvas, startX, startY, pairs, size)
        # Calculate StartY co-ordinate of the next row
       startY = startY + size
        # Calculate if next row should be offsetted else set startX to original startX value
       if offset == True:
          startX = startX + offset
       else:
          startX = originalStartX


def initialise():
   pass


def mainBody():
    # Create a panel 650 x 400
    panel = DrawingPanel(650,400)

    # Set panel tittle to CafeWall
    panel.title("Solution: CafeWall")

    # Se background colour to Grey
    panel.set_background("Grey")

    # Create canvas object
    canvas = panel.canvas  
    # Draw upper-left figure
    drawRow(canvas, 0, 0, 4, 20)
    # Draw mid-left figure    
    drawRow(canvas, 50, 70, 5, 30)
    # Draw lower-left figure
    drawGrid(canvas, 10, 150, 4, 25, 0, 8)
    # Draw lower-left figure
    drawGrid(canvas, 250, 200, 3, 25, 10, 6)
    # Draw lower-right figure
    drawGrid(canvas, 425, 180, 5, 20, 10, 10)
    # Draw upper-right figure
    drawGrid(canvas, 400, 20, 2, 35, 35, 4)
    
        
def terminate():
    pass


def main():
    initialise()
    mainBody()
    terminate()
          

main()
