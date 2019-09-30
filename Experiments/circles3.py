import rhinoscriptsyntax as rs
import random



stretch = 2
centerX = 0
centerY = 0

for rows in range (0,7,1):
    for circles in range (0,10,1):
        if (stretch > .5 and stretch < 3):
            stretch+= random.uniform(-.5,.5)
        else:
            stretch = 1
        circ = rs.AddEllipse((centerX,centerY,0),stretch,stretch)
        centerX+=random.uniform(7,9)

    if (rows % 2==1):
        centerX = 0
    else:
        centerX = 2
    centerY += 7
