import numpy as np

a = np.array([[5,3,4],[1,5,8],[6,4,2]])

b = np.array([[8,3,4],[1,5,9],[6,7,2]])
d = a-b
print(np.sum(abs(d)))