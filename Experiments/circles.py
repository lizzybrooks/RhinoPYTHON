import rhinoscriptsyntax as rs
import random



stretch = 10
centerX = 0
centerY = 0

for circles in range (0,15,1):
    circ = rs.AddEllipse((centerX,centerY,0),10,stretch)
    centerX += 1
    stretch += 1
