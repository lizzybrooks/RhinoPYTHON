import rhinoscriptsyntax as rs

circle = rs.AddEllipse((0,0,0),40,40)

def spirograph(x,y):
    for squares in range (1,360,10):
        spot=rs.AddRectangle((x,y,0),10,10)
        rs.RotateObject(spot,(x,y,0),squares,None,copy=False)

spirograph(0,40)
spirograph(-40,0)
spirograph(0,-40)
spirograph(40,0)



points = [(0,0,0),(5,5,0),(5,10,0),(0,15,0),(-5,10,0),(0,0,0)]

for angle in range(1,360,50):
    shape = rs.AddPolyline(points, replace_id=None)
    rs.RotateObject(shape,(0,0,0),angle,None,copy=True)
