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
length = 7*large_major
width = 2*large_major+6*small_major
height = 230

# Depth of rows
row_height = 50

col = large_major

center = 0
factor = 1.5
lg_center = factor*center

large_hole_distance = [-6/3*col-lg_center, -2/3*col-lg_center, 2/3*col+lg_center, 6/3*col+lg_center]
small_hole_distance = [-5/2*col-center, -3/2*col-center, -1/2*col-center, 1/2*col+center, 3/2*col+center, 5/2*col+center]
row_distance = [2*large_major, 2*large_major+2*small_major, 2*large_major+4*small_major]

with BuildPart() as bp:
    # "https://build123d.readthedocs.io/en/latest/objects.html#objects_part.Box"
    # fillet(objects=bp.edges().filter_by(Axis.Z), radius=2)

    # Main box
    Box(length, width, height) 

    # Cut Rows

    for e,i in enumerate(row_distance):
        with Locations((0, -i, height/2)):
            Box(length, width, (e+1)*row_height, mode=Mode.SUBTRACT)

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

    # Cut Underneath
    walls = 10
    for i in range(4):
        with Locations((0, 2*i*small_major, -height/2)):
            Box(length-2*walls, width, 2*height-row_height*(4-i), mode=Mode.SUBTRACT)

print(length, width, height)

# Show in OCP CAD viewer
show(bp)

# Export using build123d's export functionality
export_stl(bp.part, "../generated-cad/paint_stand.stl")
export_step(bp.part, "../generated-cad/paint_stand.step")
