from build123d import *
from ocp_vscode import show

length, width, height = 280, 254, 230

mid_drop = 30
bot_drop = 30

large_hole = 26 
large_hole_width = 26/2
large_hole_length = 64/2 
small_hole = 19 # 51 length
small_hole_width = 19/2 # 51 length
small_hole_length = 51/2 # 51 length

row1 = width/2 - large_hole_width*3
row_height = 50

col = length/2-large_hole_length*3

hole_distance = [-5/2*col, -3/2*col, -col/2, col/2, 3/2*col, 5/2*col]

with BuildPart() as bp:
    # "https://build123d.readthedocs.io/en/latest/objects.html#objects_part.Box"
    # fillet(objects=bp.edges().filter_by(Axis.Z), radius=2)

    # Main box
    Box(length, width, height) 

    # Cut Rows
    with Locations((0, -width* 3/10, height/2)):
        Box(length, width, row_height, mode=Mode.SUBTRACT)

    with Locations((0, -width* 5/10, height/2)):
        Box(length, width, row_height*2, mode=Mode.SUBTRACT)

    with Locations((0, -width* 7/10, height/2)):
        Box(length, width, row_height*3, mode=Mode.SUBTRACT)

    # Row 1 - Large Holes

    with BuildSketch() as bs:
        with Locations((0, row1)):
            Ellipse(large_hole_width,large_hole_length, 45)
    extrude(amount=height, mode=Mode.SUBTRACT)

    with BuildSketch() as bs:
        with Locations((-col, row1)):
            Ellipse(large_hole_width,large_hole_length, 45)
    extrude(amount=height, mode=Mode.SUBTRACT)

    with BuildSketch() as bs:
        with Locations((col, row1)):
            Ellipse(large_hole_width,large_hole_length, 45)
    extrude(amount=height, mode=Mode.SUBTRACT)

    # Row 2 - Small Holes

    
    for i in distance:
        with BuildSketch() as bs:
            with Locations((i, 25)):
                Ellipse(small_hole_width,small_hole_length, 45)
        extrude(amount=height, mode=Mode.SUBTRACT)

    # Row 3 - Small Holes

    with BuildSketch() as bs:
        with Locations((0, -25)):
            Ellipse(small_hole_width,small_hole_length, 45)
    extrude(amount=height, mode=Mode.SUBTRACT)

    with BuildSketch() as bs:
        with Locations((-col, -25)):
            Ellipse(small_hole_width,small_hole_length, 45)
    extrude(amount=height, mode=Mode.SUBTRACT)

    with BuildSketch() as bs:
        with Locations((col, -25)):
            Ellipse(small_hole_width,small_hole_length, 45)
    extrude(amount=height, mode=Mode.SUBTRACT)

    # Row 4 - Small Holes

    with BuildSketch() as bs:
        with Locations((0, -75)):
            Ellipse(small_hole_width,small_hole_length, 45)
    extrude(amount=height, mode=Mode.SUBTRACT)

    with BuildSketch() as bs:
        with Locations((-col, -75)):
            Ellipse(small_hole_width,small_hole_length, 45)
    extrude(amount=height, mode=Mode.SUBTRACT)

    with BuildSketch() as bs:
        with Locations((col, -75)):
            Ellipse(small_hole_width,small_hole_length, 45)
    extrude(amount=height, mode=Mode.SUBTRACT)


# Show in OCP CAD viewer
show(bp)

# Export using build123d's export functionality
# export_stl(bp.part, "../generated-cad/rounded_box.stl")
# export_step(bp.part, "../generated-cad/rounded_box.step")
