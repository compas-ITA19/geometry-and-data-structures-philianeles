from compas.geometry import Point
from compas.geometry import Vector
from compas.geometry import Plane
from compas.geometry import Frame

def arbitrary_vector_in_plane(point,vector):
    my_frame = Frame.from_plane(Plane(point,vector))
    result = my_frame[1]*5
    return result

P = Point(0,0,0)
V = Vector(0,0,1)
print arbitrary_vector_in_plane(P,V)
