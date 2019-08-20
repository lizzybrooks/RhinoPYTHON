import rhinoscriptsyntax as rs
import random
import math




def leaf (x,y):
    point1 = [x,y,0]
    point2 = [x+5,y+10,0]
    point3 = [x+10,y+10,0]

    curvePoints = [point1,point2,point3]

    rs.AddInterpCurve(curvePoints,3)

    point1 = [x,y,0]
    point2 = [x+10,y+5,0]
    point3 = [x+10,y+10,0]

    curvePoints = [point1,point2,point3]

    rs.AddInterpCurve(curvePoints,5)

x=0
y=0
for c in range (0,20)
    leaf(x,y)
    
