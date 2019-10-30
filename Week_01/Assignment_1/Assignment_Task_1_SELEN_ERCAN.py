from compas.geometry import Point
from compas.geometry import Vector


def is_ccw(A,B,C):
    Vector_AB = Vector.from_start_end(A,B)
    Vector_AC = Vector.from_start_end(A,C)

    #Tests whether rotation from AB onto AC is ccw in the xy-plane
    angle = Vector.angle_signed(Vector_AB,Vector_AC,(0,0,1))
    if angle < 0:
        return False
    else:
        return True


A_pt = Point(0,0,0)
B_pt = Point(2,5,0)
C_pt = Point(-5,4,0)

print (is_ccw(A_pt,B_pt,C_pt))

