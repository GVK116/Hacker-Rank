import numpy


def matrix(arr):
    return  numpy.reshape(numpy.array(arr,int),(3,3))


arr = input().strip().split()

result = matrix(arr)
print(result)

