# Count all possible paths from top left to bottom of m X n matrix

import numpy
arr = numpy.zeros((5,5))

# print(len(arr))

def track(arr,i,j,d):
    if i >len(a) or j>len(a):
        return 0
    if i == d and j ==d:
        return 1
    ways = track(arr,i+1,j,d)+track(a,i,j+1,d)
    return ways



print(track(a,0,0,4))

