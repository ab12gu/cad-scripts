## Table Ratcheting Hinge
#
# by: Abhay Gupta
# date created: 25-10-16
#
# https://build123d.readthedocs.io/en/latest/introductory_examples.html

from build123d import *
from ocp_vscode import show

length = 256
thickness = 50.8
width = 101.6

with BuildPart() as hinge_p:
    with BuildSketch() as hinge_sk:
        with BuildLine() as hinge_ln:
            l1 = Line((0,0), (length, 0))
            l2 = Line((length,0), (length, width))
            l3 = Line((length,width), (0, width))
            l4 = Line((0,width), (0, 0))
        make_face()
    extrude(amount=thickness)


# Show in OCP CAD viewer
#show(ex4)
show(hinge_p)

# Export using build123d's export functionality
#export_stl(bp.part, "../generated-cad/paint_stand.stl")
#export_step(bp.part, "../generated-cad/paint_stand.step")
