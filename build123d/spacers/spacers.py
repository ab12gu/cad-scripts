
from build123d import *
from ocp_vscode import show_all

def main():
    length = 16
    outer_diameter = 16
    inner_diameter = 6

    spacer = Cylinder(outer_diameter/2, length) - Cylinder(inner_diameter/2, length)

    #export_stl()
    export_stl(spacer, "bike_caliper_spacer.stl")
    show_all()


if __name__ == "__main__":
    main()
