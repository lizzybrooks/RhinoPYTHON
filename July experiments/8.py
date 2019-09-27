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

    for point in range (1, sides, 1):
        anothercorner = rs.RotateObject(cornerpoint,(0,0,0),point*360/sides,None,copy=True)
        cornerpoints.append(anothercorner)

    #print(cornerpoints)

    for item in range (0,len(cornerpoints)-1,1):
        rs.AddLine(cornerpoints[item],cornerpoints[item+1])

    rs.AddLine(cornerpoints[len(cornerpoints)-1],cornerpoints[0])


equilateralPolygon(6,5)
equilateralPolygon(10,4)
equilateralPolygon(3,3)
