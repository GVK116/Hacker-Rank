import numpy

def SumofProduct(arr):
    return numpy.product(numpy.sum(numpy.array(arr,int),axis=0))


n,m = map(int,input().split())
array = []

for _ in range(n):
    array.append(input().split())

result = SumofProduct(array)
print(result)