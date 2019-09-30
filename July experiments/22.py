import rhinoscriptsyntax as rs
import random


aCircle = rs.AddEllipse((random.uniform(5,10),0,0),1,1)



def circleLine(start,end):
    circles = []
    for c in range (start,end,1):
        anotherCircle = rs.AddEllipse((c,c,0),random.uniform(1,2),random.uniform(1,2))
        circles.append(anotherCircle)
    rs.AddObjectsToGroup(circles, "lottacircles")
    print(circles)

mz=circleLine(9,14)

obj = aCircle
# start = (0,0,0)
# end = (4,4,0)
# if start and end:
rs.MirrorObject( obj, (0,0,0),(4,4,0), True )
