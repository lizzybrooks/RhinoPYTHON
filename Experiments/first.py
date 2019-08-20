import rhinoscriptsyntax as rs
import random
import math

centerCircle = rs.AddEllipse(rs.WorldXYPlane(),10 ,10.0)


points = []
for p in range (10):
    point = rs.GetPointOnCurve(centerCircle, "Point on curve")
    rs.AddPoint(point)
    points.append(point)

print(points)


def coolCurvy(x,y):
    curvePoints = [(x,y,0),(x+10,y-5,0),(x+20,y+10,0),(x+30,y-10,0),(x+25,y,0)]
    return rs.AddCurve(curvePoints,3)


for p in range(len(points)):
    a = coolCurvy(points[p][0],points[p][1])
    if points[p][0]<0:
        rs.RotateObject(a, (points[p][0],points[p][1],0), 180, None, copy=False)

#one cool prompt:If the center of a circle is inside the previous circle, make a new circle of random size
#overlapping circles will make a nice sticker!

#OR, instead of a curve coming out of the edge of the circle, do a triangle. Then a line, then a diamond, then another circle... That is your mandala.

# you need to figure out how to automate the points on the edge of the circle, though. 
