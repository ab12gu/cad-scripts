'''
filename: bottle_mount.py
Assume units are mm

'''

from build123d import * 
from ocp_vscode import show

class BottleMount:
    def __init__(self):
        pass

    def generate(self):
        print("Generating a cad bottle mount!")

        bolt_distance = 64.0

        length, width = bolt_distance * 2.5, bolt_distance * 2.0
        thickness = 10.0

        with BuildPart() as ex1:
            Box(length, width, thickness)
            rotated_box = Rotation(45, 0, 0) * Box(length, width, thickness)

if __name__ == "__main__":

    bottlemount = BottleMount()
    bottlemount.generate()
