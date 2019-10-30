Vector_1 = [5.0, 5.0, 6.0]
Vector_2 = [5.0, -7.0, 8.0]

def cross_product(Vector_1, Vector_2):
    return [Vector_1[1] * Vector_2[2] - Vector_1[2] * Vector_2[1], 
            Vector_1[2] * Vector_2[0] - Vector_1[0] * Vector_2[2], 
            Vector_1[0] * Vector_2[1] - Vector_1[1] * Vector_2[0]]

print "Cross product of two given vectors = ", cross_product(Vector_1, Vector_2)


def unitize(Vector_R):
    if Vector_R[0] != 0:
        Vector_R_unit_X = Vector_R[0] / abs(Vector_R[0])
    else:
        Vector_R_unit_X = 0
    if Vector_R[1] != 0:
        Vector_R_unit_Y = Vector_R[1] / abs(Vector_R[1])
    else:
        Vector_R_unit_Y = 0
    if Vector_R[2] != 0:
        Vector_R_unit_Z = Vector_R[2] / abs(Vector_R[2])
    else:
        Vector_R_unit_Z = 0
    return [Vector_R_unit_X,0,0],[0,Vector_R_unit_Y,0],[0,0,Vector_R_unit_Z]


Vector_R = cross_product(Vector_1, Vector_2)

print "Set of three orthonormal vectors = ", unitize(Vector_R)
