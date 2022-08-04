#Diagonal Difference
#https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    lArr = len(arr);
    diag1 = 0;
    diag2 = 0;
    for i in range(lArr):
        diag1 += arr[i][i];
        diag2 += arr[i][(lArr-1)-i];
    
    return (abs(diag1-diag2));

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#NOTA:
'''
Se puede realizar el código solo con un contador y precindir de diag1 y diag2. Ya que los dos valores de cada diagonal se deben sumar al final (de todos modos) con una variable Total, simplemente se suma cada valor de la diagonal 1 y se resta cada valor de la diagonal 2.
'''