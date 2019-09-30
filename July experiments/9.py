import rhinoscriptsyntax as rs
import random



def equilateralPolygon(sides,size,centerX,centerY):
    centerpoint = (centerX,centerY,0)
    cornerpoints=[]
    cornerpoint=rs.AddPoint(centerX,centerY+size,0)
    cornerpoints.append(cornerpoint)

    for point in range (1, sides, 1):
        anothercorner = rs.RotateObject(cornerpoint,centerpoint,point*360/sides,None,copy=True)
        cornerpoints.append(anothercorner)

    #print(cornerpoints)

    for item in range (0,len(cornerpoints)-1,1):
        rs.AddLine(cornerpoints[item],cornerpoints[item+1])

    rs.AddLine(cornerpoints[len(cornerpoints)-1],cornerpoints[0])


equilateralPolygon(6,5,0,0)
equilateralPolygon(10,4,4,9)
equilateralPolygon(3,3,5,17)
