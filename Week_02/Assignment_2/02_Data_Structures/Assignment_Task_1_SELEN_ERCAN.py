from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist

from random import choice

my_mesh = Mesh.from_obj("C:\\Users\\sercan\\Documents\\GitHub\\compas-dev\\packages\\ITA19\\modules\\module0\\02_datastructures_and_geometry\\data\\faces.obj")

boundary = list(my_mesh.is_vertex_on_boundary(key) for key in my_mesh.vertices())
boundary_key = []
for i,key in enumerate(my_mesh.vertices()):
    if boundary[i] == True:
        boundary_key.append(key)


#start_key = choice(boundary_key)
start_key = 34
print start_key
path = [start_key]

faces = my_mesh.vertex_faces(path[-1],ordered=True)
print faces
for face in faces:
    print my_mesh.face_vertices(face)


find_path = True
safety = 0
while find_path and safety < 2:
    safety += 1
    faces = my_mesh.vertex_faces(path[-1],ordered=True)
    print faces
    common_ver = my_mesh.face_vertices(faces[0])
    print common_ver
    path.append(common_ver[0])



artist = MeshArtist(my_mesh)
artist.draw_vertices(
color={key: (255, 0, 0) for key in common_ver})

artist.draw_vertexlabels(
text={key: str(key) for key in common_ver})
