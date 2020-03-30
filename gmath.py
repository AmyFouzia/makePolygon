import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    mag = sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    vector[0] = vector[0]/mag
    vector[1] = vector[1]/mag
    vector[2] = vector[2]/mag

#Return the dot porduct of a . b
def dot_product(a, b):
    return (a[0] * b[0] + a[1] * b[1] + a[2] * b[2])

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    a = [polygons[i+1][0]-polygons[i][0],polygons[i+1][1]-polygons[i][1],polygons[i+1][2]-polygons[i][2]]
    b = [polygons[i+2][0]-polygons[i][0],polygons[i+2][1]-polygons[i][1],polygons[i+2][2]-polygons[i][2]]
    ans = [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
    return ans
