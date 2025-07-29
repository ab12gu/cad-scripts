from build123d import *
from ocp_vscode import show

with BuildPart() as bp:
    Box(20, 30, 10) # length, width, height
    fillet(objects=bp.edges().filter_by(Axis.Z), radius=2)

# Show in OCP CAD viewer
show(bp)

# Export using build123d's export functionality
export_stl(bp.part, "rounded_box.stl")
export_step(bp.part, "rounded_box.step")
