import rhinoscriptsyntax as rs
import random
import math


point1 = [0,0,0]
point2 = [5,10,0]
point3 = [10,10,0]

curvePoints = [point1,point2,point3]

rs.AddInterpCurve(curvePoints,3)

point1 = [0,0,0]
point2 = [10,5,0]
point3 = [10,10,0]

curvePoints = [point1,point2,point3]

rs.AddInterpCurve(curvePoints,5)
