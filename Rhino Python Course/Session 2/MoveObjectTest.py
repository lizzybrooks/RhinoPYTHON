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


whereIsBlip = random.randint(0,9)
for c in range(10):
	aCurve = blipCurve(c)
	rs.MirrorObject(aCurve, (0,0,0),(0,40,0),True)
	# if c == whereIsBlip:
	# 	rs.MoveObject(aCurve, (0,0,random.uniform(-100,-50)))
	# 	rs.MirrorObject(aCurve, (0,0,0),(0,0,10))
