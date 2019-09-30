import rhinoscriptsyntax as rs
import random
import math

# centerCircle = rs.AddEllipse(rs.WorldXYPlane(),10 ,10.0)
# obj = rs.GetObject("Pick a curve")
# if rs.IsCurve(obj):
#     point = rs.GetPointOnCurve(obj, "Point on curve")
#     if point: rs.AddPoint(point)

obj = rs.GetObject("Pick a curve")
points = []
for p in range (10):
    point = rs.GetPointOnCurve(obj, "Point on curve")
    rs.AddPoint(point)
    points.append(point)

print(points)
