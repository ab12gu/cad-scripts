## Table Ratcheting Hinge
#
# by: Abhay Gupta
# date created: 25-10-16
#
# https://build123d.readthedocs.io/en/latest/introductory_examples.html

from build123d import *
from ocp_vscode import show

inch = 25.4
length = inch*10-inch
thickness = inch*2
width = inch*4

with BuildPart() as hinge_p:
    with BuildSketch() as hinge_sk:

        with BuildLine() as hinge_ln:
            l1 = Line((0,0), (length, 0))
            l2 = Line((length,0), (length, width))
            l3 = Line((length,width), (0, width))
            l4 = Line((0,width), (0, 0))
        make_face()

        with Locations((length-2*inch,inch)):
            Circle(inch/4,mode=Mode.SUBTRACT)

        with Locations((2*inch,inch)):
            Circle(inch/4,mode=Mode.SUBTRACT)
        
        for i in range(3):
            with Locations((3*inch*i+3/2*inch,width-inch)):
                Circle(inch,mode=Mode.SUBTRACT)
            with Locations((3*inch*i+3/2*inch,width)):
                Rectangle(2*inch,2*inch,mode=Mode.SUBTRACT)
    extrude(amount=thickness)

    with BuildSketch(Plane.XZ) as triangle_sk:
        with Locations((inch/4,inch)):
            RegularPolygon(radius=inch/2, side_count=3)
    extrude(amount=-thickness, mode=Mode.SUBTRACT)

    with BuildSketch(Plane.XZ) as triangle_sk:
        with Locations((inch/4+length,inch)):
            RegularPolygon(radius=inch/2, side_count=3)
    extrude(amount=-thickness)







# Show in OCP CAD viewer
#show(ex4)
#show(hinge_sk)
show(hinge_p)

# Export using build123d's export functionality
#export_stl(bp.part, "../generated-cad/paint_stand.stl")
#export_step(bp.part, "../generated-cad/paint_stand.step")
