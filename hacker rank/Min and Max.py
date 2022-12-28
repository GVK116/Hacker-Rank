import numpy

n,m = map(int,input().split())
arr = []

for i in range(n):
    arr.append(input().split())

arr = numpy.array(arr,int)
print(numpy.max(numpy.min(numpy.array(arr,int),axis=1),axis=0))