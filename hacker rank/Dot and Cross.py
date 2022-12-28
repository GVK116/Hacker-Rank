import numpy as np

n = int(input())

A,B = [],[]
for _ in range(n):
    A.append(input().split())
for _ in range(n):
    B.append(input().split())
A,B = np.array(A,int),np.array(B,int)
print(np.dot(A,B))