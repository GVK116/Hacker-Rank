import numpy


def Concatenate(array1,array2):
    return numpy.concatenate((numpy.array(array1,int),numpy.array(array2,int)))



n,m,p = map(int, input().split())

array1,array2 = [],[]
for _ in range(n):
    array1.append(input().split())
for _ in range(m):
    array2.append(input().split())

result = Concatenate(array1,array2)
print(result)