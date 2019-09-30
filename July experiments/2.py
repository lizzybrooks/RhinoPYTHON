import rhinoscriptsyntax as rs
import random


# aCircle = rs.AddEllipse((0,0,0),1,1)

for c in range (0,10,1):
    rs.AddEllipse((c,c,0),random.uniform(1,2),random.uniform(1,2))
