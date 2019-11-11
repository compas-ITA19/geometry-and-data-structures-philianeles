from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist

from random import choice

my_mesh = Mesh.from_obj("C:\\Users\\sercan\\Documents\\GitHub\\compas-dev\\packages\\ITA19\\modules\\module0\\02_datastructures_and_geometry\\data\\faces.obj")


boundary = list(my_mesh.is_vertex_on_boundary(key) for key in my_mesh.vertices())
boundary_key = []
for i,key in enumerate(my_mesh.vertices()):
    if boundary[i] == True:
        boundary_key.append(key)


start_key = choice(boundary_key)
#start_key = 1


path = [start_key]
neighbours = my_mesh.vertex_neighbors(start_key)

current_key = start_key
for n in neighbours:
    if not my_mesh.is_vertex_on_boundary(n):
        previous_key, current_key = current_key, n
        break

while True:
    path.append(current_key)
    if my_mesh.is_vertex_on_boundary(current_key):
        break
    neighbours = my_mesh.vertex_neighbors(current_key, ordered=True)
    i = neighbours.index(previous_key)
    previous_key, current_key = current_key, neighbours[i - 2]

print(path)


#visualize
artist = MeshArtist(my_mesh)
#artist.draw_vertices(
#color={key: (255, 0, 0) for key in boundary_key})

artist.draw_vertices(path,
color={key: (255, 0, 0) for key in [start_key]})
#artist.draw_vertices(neighbours)

artist.draw_edges()
artist.draw_faces()

#artist.draw_vertexlabels(
#text={key: str(key) for key in boundary_key},color={start_key: (255, 0, 0)})

#artist.draw_vertexlabels(
#text={key: str(key) for key in [start_key]},color={start_key: (255, 0, 0)})

artist.draw_vertexlabels(
text={key: str(key) for key in path},color={key: (255, 0, 0) for key in path})
