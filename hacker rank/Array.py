import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    a = list(numpy.array(arr,float))
    return numpy.flip(a)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)