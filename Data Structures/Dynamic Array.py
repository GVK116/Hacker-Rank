#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    l = [[] for _ in range(n)]
    latsans = 0
    result = []
    for _ in range(len(queries)):
        a,x,y = queries[_]
        if a ==1:
            l[(x^latsans)%n].append(y)
        else:
            t = (x^latsans)%n
            latsans = l[t][y%len(l[t])]
            result.append(latsans)
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    # fptr.write('\n'.join(map(str, result)))

    ab = ' '.join(map(str, result))

    print(ab)

    # fptr.write('\n')
    #
    # fptr.close()
