import rhinoscriptsyntax as rs
import random
import math


def lazyLeaf(z):

	lazyPoints = [(0,0,z)]



	for q in range (0,100,5):
		if q== 10:
			newX = 70
			newY=20
		elif q == 20:
			newX = 20
			newY = 50
		elif q == 40:
			newX = random.uniform(60,90)+q
			newY = random.uniform(10,20)+q
		elif q == 45:
			newX = random.uniform(60,90)+q
			newY = random.uniform(30,40)+q
		else:
			newX = random.uniform(0,30) + q
			newY = random.uniform(30,40) + q
		lazyPoints.append((newX,newY,z))

	lazyPoints.append((40,150,z))

	for smooth in range(100,0,-5):
		newX = math.sin(smooth)
		newY = smooth
		lazyPoints.append((newX,newY,z))

	lazyPoints.append((0,0,z))

	return rs.AddInterpCurve(lazyPoints,3)

for c in range (-25,25,1):
	x = 40
	y = 50
	oneLeaf = lazyLeaf(c)
	rs.MoveObject(oneLeaf, (c,c,c))
