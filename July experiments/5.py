import rhinoscriptsyntax as rs


for squares in range (1,360,30):
    spot=rs.AddRectangle((0,40,0),10,10)
    rs.RotateObject(spot,(0,0,0),squares,None,copy=False)
