import rhinoscriptsyntax as rs
import random


def LEAF (startX,startY, width):
    rotationAngle = random.uniform(40,140)
    halfLeaf = rs.AddArc3Pt((startX,startY,0),(startX,startY+12,0),(startX+width,startY+4,0))
    secondHalf = rs.MirrorObject(halfLeaf,(startX,startY,0),(startX,startY+12,0),copy=True)

    rs.RotateObject(halfLeaf,(startX,startY,0),rotationAngle,axis=None, copy=False)
    rs.RotateObject(secondHalf, (startX,startY,0),rotationAngle,axis=None, copy=False)

    veinPoints = [(startX,startY,0)]
    widthFixer = 2.2

    for points in range (1,12,2):
        veinPoint = (startX + random.uniform(-1,1),startY+points,0)
        veinPoints.append(veinPoint)
        # rs.AddPoint(veinPoint)

        if(points<7):
            points = (startX-width+widthFixer, startY+points + random.uniform(-.5,.5),0),veinPoint, (startX+width-widthFixer, startY+points + random.uniform(-.5,.5),0)
            vein = rs.AddCurve(points)
            rs.RotateObject(vein, (startX,startY,0),rotationAngle,axis=None, copy=False)
            widthFixer = widthFixer - 1
            print(widthFixer)
        elif(points == 7):
            widthFixer = .2
            points = (startX-width + widthFixer, startY+points + random.uniform(-.5,.5),0),veinPoint, (startX+width-widthFixer, startY+points + random.uniform(-.5,.5),0)
            vein = rs.AddCurve(points)
            rs.RotateObject(vein, (startX,startY,0),rotationAngle,axis=None, copy=False)

        elif (points>7):
            widthFixer = widthFixer + 1
            points = (startX-width + widthFixer, startY+points + random.uniform(-.5,.5),0),veinPoint, (startX+width-widthFixer, startY+points + random.uniform(-.5,.5),0)
            vein = rs.AddCurve(points)
            rs.RotateObject(vein, (startX,startY,0),rotationAngle,axis=None, copy=False)
            print(widthFixer)

    middleVein = rs.AddInterpCurve(veinPoints)
    rs.RotateObject(middleVein, (startX,startY,0),rotationAngle,axis=None, copy=False)


def branch (startX,startY):
    branchPoints = [(startX,startY,0)]
    yValue = []
    for knots in range (0,100,10):
        branchPointsY = startY+knots
        yValue.append(branchPointsY)
        newKnot = (startX + random.uniform(-1,1),branchPointsY,0)
        branchPoints.append(newKnot)


    curvybranch =  rs.AddInterpCurve(branchPoints)

    for leaves in range (0,len(branchPoints)):
        LEAF(0,yValue[leaves],random.uniform(2,4))

branch(0,0)
branch(20,15)

# LEAF(0,0,3)
#
# LEAF(6,8,4)



# points = (0,0,0), (3,3,0), (3,6,0), (0,10,0)
# rs.AddInterpCurve(points)
