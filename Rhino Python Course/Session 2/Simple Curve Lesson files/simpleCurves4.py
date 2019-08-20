import rhinoscriptsyntax as rs
import random
import math

def leftLeaf(x,y):
    point1 = [x,y,0]
    point2 = [x+5,y+10,0]
    point3 = [x+10,y+10,0]

    leftPoints = [point1,point2,point3]

    return rs.AddInterpCurve(leftPoints,3)

def rightLeaf (x,y):
    point1 = [x,y,0]
    point2 = [x+10,y+5,0]
    point3 = [x+10,y+10,0]

    rightPoints = [point1,point2,point3]

    return rs.AddInterpCurve(rightPoints,5)

def LEFTflipLeaf(x,y):
    point1 = [x,y,0]
    point2 = [x-5,y+10,0]
    point3 = [x-10,y+10,0]

    leftPoints = [point1,point2,point3]

    return rs.AddInterpCurve(leftPoints,3)

def RIGHTflipLeaf (x,y):
    point1 = [x,y,0]
    point12 = [x-random.uniform(20,50),y-5,0]
    point2 = [x-10,y+5,0]
    point3 = [x-10,y+10,0]

    rightPoints = [point1,point12,point2,point3]

    return rs.AddInterpCurve(rightPoints,5)

def flipLeaf(x,y):
    LEFTflipLeaf(x,y)
    RIGHTflipLeaf(x,y)

def leaf(x,y):
    rightLeaf(x,y)
    leftLeaf(x,y)


x=1
for c in range (-100,80,14):
    flipLeaf(x,c)
    leaf(x,c)
    x=x*1.5
