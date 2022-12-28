import numpy

def Floor(arr):
    print(numpy.floor(arr))

def Ceil(arr):
    print(numpy.ceil(arr))

def Rint(arr):
    a = numpy.rint(arr)


A = input().split()
arr = numpy.array(A,float)

print(arr)
Floor(arr)
Ceil(arr)
Rint(arr)