import rhinoscriptsyntax as rs
import random
import math

count = 0
xcenter = 0
ycenter = 0
zcenter = 0

while count < 10000:
    x = random.uniform(xcenter-10,xcenter+10)
    y = random.uniform(ycenter-10,ycenter+10)
    z = random.uniform(zcenter-10,zcenter+10)

    point = (x,y,z)

    if rs.Distance(point, (0,0,0)) < 7 :
        rs.AddPoint(point)
        count = count + 1

z = 0
radius = 0
theta = 0
count = 0
radiusChange = .001
countingUp = 1


while z <= 100:
        if count % 2 == 0:
            x = (radius+4) * math.cos(theta)
            y = (radius+4) * math.sin(theta)

        else:
            x = radius * math.cos(theta)
            y = radius * math.sin(theta)

        rs.AddPoint(x,y,z)



        theta += 1
        z = z + .01
        count += 1

        if countingUp == 1:
            radiusChange = radiusChange * 1.001
            radius += radiusChange
            if radiusChange > .029:
                countingUp = -countingUp
        elif countingUp == -1:
            radius -= .003

while z > 100 and z <= 150:
    if count % 2 == 0:
        x = (radius+4) * math.cos(theta)
        y = (radius+4) * math.sin(theta)

    else:
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

    rs.AddPoint(x,y,z)
    
    theta += 1
    z = z + .01
    count += 1

count = 0
xcenter = 0
ycenter = 0
zcenter = 150

while count < 10000:
    x = random.uniform(xcenter-20,xcenter+20)
    y = random.uniform(ycenter-20,ycenter+20)
    z = random.uniform(zcenter-20,zcenter+20)

    point = (x,y,z)

    if rs.Distance(point, (0,0,150)) < 17 :
        rs.AddPoint(point)
        count = count + 1
