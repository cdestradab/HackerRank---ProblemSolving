#!/bin/python3

import math
import os
import random
import re
import sys
import itertools as it;
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sums = [sum(x) for x in it.permutations(arr, 4)];
    print(min(sums), max(sums));

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)

#OTRA APROXIMACIÓN:
#No importa el orden de las permutaciones, siempre la suma mas grande será la que no tenga al número mas pequeño, y la menor suma será la que no tenga al número mas grande.
'''
lst = map(int,input().strip().split(' '))
x = sum(lst)
print (x-(max(lst))), (x-(min(lst)))
'''