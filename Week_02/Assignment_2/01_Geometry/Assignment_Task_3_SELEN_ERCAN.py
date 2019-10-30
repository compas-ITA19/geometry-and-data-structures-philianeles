# cross product of two arrays of vectors with the same length
def cross_product_array(Vector_arr_1, Vector_arr_2):
    cross_product = []
    for i in range(len(Vector_arr_1)):
        cross_product.append([Vector_arr_1[i][1]*Vector_arr_2[i][2] - Vector_arr_1[i][2]*Vector_arr_2[i][1],
                              Vector_arr_1[i][2]*Vector_arr_2[i][0] - Vector_arr_1[i][0]*Vector_arr_2[i][2],
                              Vector_arr_1[i][0]*Vector_arr_2[i][1] - Vector_arr_1[i][1]*Vector_arr_2[i][0]])
    return cross_product

Vector_arr_1 = [(1,2,3), (4,5,6)]
Vector_arr_2 = [(4,5,6), (1,2,3)]

print cross_product_array(Vector_arr_1, Vector_arr_2)


#numpy equivalent
import numpy as np

Vector_arr_1 = np.array([(1,2,3), (4,5,6)])
Vector_arr_2 = np.array([(4,5,6), (1,2,3)])

print (np.cross(Vector_arr_1,Vector_arr_2))
