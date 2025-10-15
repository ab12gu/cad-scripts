from build123d import *
from ocp_vscode import show

length, width, height = 280, 254, 230

mid_drop = 30
bot_drop = 30

large_hole = 26 # 64 length
small_hole = 19 # 51 length

with BuildPart() as bp:
    # "https://build123d.readthedocs.io/en/latest/objects.html#objects_part.Box"
    Box(length, width, height) 
    Box(280, 190, 50, mode=Mode.SUBTRACT)
    # fillet(objects=bp.edges().filter_by(Axis.Z), radius=2)

    with Locations((0, 50)):
        Cylinder(radius=large_hole / 2, height=300, mode=Mode.SUBTRACT)

# Show in OCP CAD viewer
show(bp)

# Export using build123d's export functionality
# export_stl(bp.part, "../generated-cad/rounded_box.stl")
# export_step(bp.part, "../generated-cad/rounded_box.step")
