import rhinoscriptsyntax as rs

import random

firstSquare = rs.AddRectangle((0,0,0),10,10)

secondSquare = rs.AddRectangle((40,50,0),10,20)

firstCircle = rs.AddEllipse(rs.WorldXYPlane(),10,10)
rs.MoveObject(firstCircle, (20,10,0))

secondCircle = rs.AddEllipse(rs.WorldXYPlane(),4,8)
rs.MoveObject(secondCircle, (random.uniform(0,15),random.uniform(0,15),0))
