from build123d import *
from ocp_vscode import show

with BuildPart() as bp:
    # "https://build123d.readthedocs.io/en/latest/objects.html#objects_part.Box"
    Box(280 ,254 ,230) # length, width, height
    # fillet(objects=bp.edges().filter_by(Axis.Z), radius=2)

# Show in OCP CAD viewer
show(bp)

# Export using build123d's export functionality
# export_stl(bp.part, "../generated-cad/rounded_box.stl")
# export_step(bp.part, "../generated-cad/rounded_box.step")
