cor_Vertices = [(0,0),(0,3),(2,7),(3,5),(4,0)]
num_Vertices = len(cor_Vertices) - 1

def area_2D_convex_polygon(num_Vertices, cor_Vertices):
    if num_Vertices < 2:
        return "not a polygon"
    else:
        area = 0
        i = 1
        j = 2
        k = 0
        while i < num_Vertices:
            area += cor_Vertices[i][0] * (cor_Vertices[j][1] - cor_Vertices[k][1])
            i = i + 1
            j = j + 1
            k = k + 1
        area += cor_Vertices[num_Vertices][0] * (cor_Vertices[num_Vertices][1] - cor_Vertices[num_Vertices-1][1])
        return abs(area) / 2.0;

print area_2D_convex_polygon(num_Vertices, cor_Vertices)