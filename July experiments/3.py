import rhinoscriptsyntax as rs
import random


rs.AddEllipse((0,0,0),10,10)

def spoke():
    rs.AddLine((0,0,0),(0,50,0))
    spot=rs.AddRectangle((0,50,0),5,5)
    rs.RotateObject(spot,(0,50,0),45,None,copy=False)

for spokes in range (1,360,30):
    rs.AddLine((0,0,0),(0,50,0))
    spot=rs.AddRectangle((0,50,0),5,5)
    rs.RotateObject(spot,(0,50,0),spokes,None,copy=False)
