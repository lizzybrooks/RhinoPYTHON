import rhinoscriptsyntax as rs
import random
import math

obj = rs.GetObject("Select object to mirror")
if obj:
    start = rs.GetPoint("Start of mirror plane")
    end = rs.GetPoint("End of mirror plane")
    if start and end:
        rs.MirrorObject( obj, start, end, True )
