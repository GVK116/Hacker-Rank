import numpy

n,m = map(int,input().split())
arr = []

for i in range(n):
    arr.append(input().split())

arr = numpy.array(arr,float)

print(numpy.mean(arr,axis=1),numpy.var(arr,axis=0),round(numpy.std(arr,axis = None),11),sep='\n')