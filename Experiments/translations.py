import rhinoscriptsyntax as rs
import random
import math

# objs = rs.GetObjects("Select objects to copy")
# if objs:
#     xform = rs.XformTranslation([10,10,0])
#     rs.TransformObjects( objs, xform, True )

mirrrred = rs.GetObjects("Select objects to mirror")
if mirrrred:
    plane = rs.ViewCPlane()
    xform = rs.XformMirror(plane.Origin, plane.Normal)
    rs.TransformObjects( mirrrred, xform, True )
