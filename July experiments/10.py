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


for shapes in range (3,7,1):
    equilateralPolygon(shapes,shapes,0,0)

for shapes in range(9,3,-1):
    equilateralPolygon(shapes,shapes-2,15,0)


for shapes in range(7,2,-1):
    equilateralPolygon(shapes,shapes,0,15)
