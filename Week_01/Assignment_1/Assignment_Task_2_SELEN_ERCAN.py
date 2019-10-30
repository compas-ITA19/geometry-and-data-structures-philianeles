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


file = open("C:\Users\sercan\Documents\GitHub\compas-dev\packages\ITA19\modules\module0\points.txt","r") 

lines_as_list = []
for line in file:
    line = line.replace("(","")
    line = line.replace(")","")
    line = line.replace(" ", "")
    line = line.rstrip()
    lines_as_list.append(line.split(","))

for sub_list in lines_as_list:
    A = Point(sub_list[0],sub_list[1],0)
    B = Point(sub_list[2],sub_list[3],0)
    C = Point(sub_list[4],sub_list[5],0)
    print(is_ccw(A,B,C))