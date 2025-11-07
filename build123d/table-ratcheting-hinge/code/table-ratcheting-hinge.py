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

hole_radius = 3

with BuildPart() as hinge_p:
    # params: length, width, height
    with Locations((length/2, width/8, 0*width/2)):
        box = Box(length,width/4,thickness)

    for i in range(10):
        with Locations((length-inch*i+inch/2,0, -inch/2)):
            hole = Cylinder(hole_radius,width,360,(90,0,0),mode=Mode.SUBTRACT)

    with BuildSketch() as hinge_sk:

        with BuildLine() as hinge_ln:
            l1 = Line((0,0), (length, 0))
            l2 = Line((length,0), (length, width))
            l3 = Line((length,width), (0, width))
            l4 = Line((0,width), (0, 0))
        make_face()

        with Locations((length-3*inch,3/2*inch)):
            Circle(hole_radius,mode=Mode.SUBTRACT)

        with Locations((3*inch,3/2*inch)):
            Circle(hole_radius,mode=Mode.SUBTRACT)
        
        for i in range(3):
            with Locations((3*inch*i+3/2*inch,width-inch)):
                Circle(inch,mode=Mode.SUBTRACT)
            with Locations((3*inch*i+3/2*inch,width)):
                Rectangle(2*inch,2*inch,mode=Mode.SUBTRACT)
    extrude(amount=thickness)

    with BuildSketch() as emboss:
        with Locations((60,10)):
            Text("by: Abhay Gupta",font_size=10)
        with Locations((48,25)):
            Text("abgup.com",font_size=10)
    extrude(amount=thickness*2, mode=Mode.SUBTRACT)
    
    #Triangle sides

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
#show(hinge_p)

# Export using build123d's export functionality
export_stl(hinge_p.part, "../generated-cad/paint_stand_wing.stl")
export_step(hinge_p.part, "../generated-cad/paint_stand_wing.step")
