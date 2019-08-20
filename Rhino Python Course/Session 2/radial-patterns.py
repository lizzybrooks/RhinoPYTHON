import rhinoscriptsyntax as rs
import random

def blipCurve(y):

	x1 = random.uniform(0,10)
	z1 = random.uniform(0,10)

	x2 = random.uniform(10,20)
	z2 = random.uniform(10,100)

	x3 = random.uniform(20,30)
	z3 = random.uniform(10,20)


	listOfPoints = [(0,y,0),(x1,y,z1),(x2,y,z2),(x3,y,z3),(0,y,0)]

	return rs.AddCurve(listOfPoints,3)


for c in range (30,360,30):
	aCurve = blipCurve(0)
	rs.RotateObject(aCurve, (0,0,0), c, None, copy=True)
# rs.MirrorObject(aCurve, (0,0,0),(0,40,0),True)
