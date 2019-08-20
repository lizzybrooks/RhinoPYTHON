import rhinoscriptsyntax as rs
import random
import math


def lazyLeaf(y):

	lazyPoints = [(0,0,0)]



	for q in range (40,100,5):
		if q == 45:
			newX = random.uniform(80,90)+q
			newZ = random.uniform(20,50)+q

		# elif q == 55:
		# 	newX = random.uniform(80,90)-q
		# 	newZ = random.uniform(20,50)+q
		else:
			newX = random.uniform(0,30) + q
			newZ = random.uniform(30,40) + q
		lazyPoints.append((newX,y,newZ))

	lazyPoints.append((40,0,150))

	for smooth in range(100,0,-5):
		newX = math.sin(smooth)
		newZ = smooth
		lazyPoints.append((newX,y,newZ))

	lazyPoints.append((0,0,0))

	print(lazyPoints)
	rs.AddInterpCurve(lazyPoints,3)


# for x in range(30):
lazyLeaf(0)
