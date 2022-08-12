#!/bin/python3

import math
import os
import random
import re
import sys
import textwrap as tw;

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(1,n+1):
        print(tw.fill("#"*i,n).rjust(n,' '));

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

#OTRA APROXIMACIÓN: @MayeulSGC
#En esta no se usa .rjust() lo que es bueno pues no se hace uso de esa función extra.
'''
def staircase(n):
    for i in range(1,n+1):
        print(' '*(n-i)+'#'*(i))
'''