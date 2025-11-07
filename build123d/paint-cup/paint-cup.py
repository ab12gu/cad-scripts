# filename: paint-cup.py
# 
# by: Abhay Gupta
# date started: 25-11-06
#
# desc: design a paint cup w/ spikes across lid
#   - for kimmy's drawing club
#   - she found it on a reddit post and wanted it
#   - using algebra mode for design


from build123d import *
from ocp_vscode import show_all
import random
import math

def main():    
    radius = 50
    height = 100
    thickness = 10

    cup = Cylinder(radius, height) \
            - Pos(0, 0, thickness) \
            * Cylinder(radius - thickness, height)

    N = 30

    for i in range(N):
        offset = 50-thickness/2
        offset2 = 10
        #rand =  random.random()
        rand = 0
        x = math.sin(i*2*math.pi/N + rand)
        y = math.cos(i*2*math.pi/N + rand)
        X = offset*x
        Y = offset*y
        X2 = (offset+offset2)*x
        Y2 = (offset+offset2)*y

        cup += Pos(X, Y, 60) * Cone(5, 0, 20)
        cup += Pos(X2, Y2, 60-12) * Rot(90,180-i*360/N,0) \
                * Cone(5, 0, 20)

        cup += Pos(X2, Y2, 60-25) * Rot(45,180-i*360/N,0) \
                * Cone(5, 0, 20)

    export_stl(cup, "paint_cup_rand.stl")
    print("Export to STL Succesfull!")

    show_all()

if __name__ == "__main__":
    main()
