## Paint stand
#
# by: Abhay Gupta
# date created: 25-10-14

from build123d import *
from ocp_vscode import show

# Paint ellipse dimensions
large_minor, large_major = 26/2, 64/2 
small_minor, small_major = 19/2, 51/2 

# Overall stand dimensions
length, width, height = 280, 2*large_major+6*small_major, 230

# Depth of rows
row_height = 50

col = length/2-large_major*3

center = 5

large_hole_distance = [-3/2*col-center, -1/2*col-center, 1/2*col+center, 3/2*col+center]
small_hole_distance = [-5/2*col, -3/2*col, -col/2, col/2, 3/2*col, 5/2*col]
row_distance = [2*large_major, 2*large_major+2*small_major, 2*large_major+4*small_major]

with BuildPart() as bp:
    # "https://build123d.readthedocs.io/en/latest/objects.html#objects_part.Box"
    # fillet(objects=bp.edges().filter_by(Axis.Z), radius=2)

    # Main box
    Box(length, width, height) 

    # Cut Rows
    for i,t in zip(row_distance, [1,2,3]):
        with Locations((0, -i, height/2)):
            Box(length, width, t*row_height, mode=Mode.SUBTRACT)

    # Row 1 - Large Holes
    for i in large_hole_distance:
        with BuildSketch() as bs:
            with Locations((i, width/2 - large_major)):
                Ellipse(large_minor,large_major, 45)
        extrude(amount=height, mode=Mode.SUBTRACT)
    
    small_rows = [width/2-(2*large_major+x) for x in [small_major, 3*small_major, 5*small_major]]
    # Row 2 - Small Holes
    for i in small_rows:
        for j in small_hole_distance:
            with BuildSketch() as bs:
                with Locations((j, i)):
                    Ellipse(small_minor,small_major, 45)
            extrude(amount=height, mode=Mode.SUBTRACT)

# Show in OCP CAD viewer
show(bp)

# Export using build123d's export functionality
# export_stl(bp.part, "../generated-cad/rounded_box.stl")
# export_step(bp.part, "../generated-cad/rounded_box.step")
