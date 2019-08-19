import rhinoscriptsyntax as rs
import random


aCircle = rs.AddEllipse((0,0,0),10,10)

for c in range (0,100,10):
    rs.AddEllipse((c,c,0),random.uniform(10,20),random.uniform(10,20))
