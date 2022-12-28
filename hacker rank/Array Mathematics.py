import numpy

def Mathematics(arrayA,arrayB):
    arrayA,arrayB = numpy.array(arrayA,int),numpy.array(arrayB,int)
    print(numpy.add(arrayA,arrayB),numpy.subtract(arrayA,arrayB),numpy.multiply(arrayA,arrayB),arrayA//arrayB,numpy.mod(arrayA,arrayB),numpy.power(arrayA,arrayB),sep='\n')


n,m = map(int,input().split())
arrayA,arrayB = [],[]

for _ in range(n):
    arrayA.append(input().split())

for _ in range(n):
    arrayB.append(input().split())

Mathematics(arrayA,arrayB)