import rhinoscriptsyntax as rs
import random


centerpoint = (0,0,0)
rs.AddPoint(centerpoint)


# cornerpoint=rs.AddPoint(0,5,0)
# for points in range(1,4,1):
#     rs.RotateObject(cornerpoint,(0,0,0),points*90,None,copy=True)


def equilateralPolygon(sides,size):
    cornerpoints=[]
    cornerpoint=rs.AddPoint(0,size,0)
    cornerpoints.append(cornerpoint)

    for points in range (1, sides, 1):
        anothercorner = rs.RotateObject(cornerpoint,(0,0,0),points*360/sides,None,copy=True)
        cornerpoints.append(anothercorner)

    print(cornerpoints)
    rs.AddLine(cornerpoints[0],cornerpoints[1])
    rs.AddLine(cornerpoints[1],cornerpoints[2])


equilateralPolygon(6,5)
