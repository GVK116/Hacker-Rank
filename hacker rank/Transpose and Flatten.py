import numpy


def Transpose(arr):
    return numpy.transpose(numpy.array(arr,int))

def Flatten(arr):
    return numpy.array(arr,int).flatten()

n,m = map(int,input().split(' '))
arr = []
for i in range(n):
    arr.append(list(input().split()))

result1 = Transpose(arr)
result2 = Flatten(arr)
print(result1,result2,sep='\n')

