import rhinoscriptsyntax as rs
import random
import math



def leaf (x,y):
    point1 = [x,y,0]
    point2 = [x+5,y+10,0]
    point3 = [x+10,y+10,0]

    leftPoints = [point1,point2,point3]

    rs.AddInterpCurve(leftPoints,3)

    point1 = [x,y,0]
    point2 = [x+10,y+5,0]
    point3 = [x+10,y+10,0]

    rightPoints = [point1,point2,point3]

    rs.AddInterpCurve(rightPoints,5)

for leaves in range (0,50,10):
    leaf(0,leaves)

    
