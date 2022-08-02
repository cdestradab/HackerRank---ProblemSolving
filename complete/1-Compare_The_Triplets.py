#Compare the triplets
#https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    pointA = 0;
    pointB = 0;
    for i in range(3):
        if a[i] == b[i]:
            continue;
        elif a[i] > b[i]:
            pointA += 1;
        elif a[i] < b[i]:
            pointB += 1;
        else:
            print("error");
            break;
    return (pointA, pointB);

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

#NOTAS:
'''
- rstrip() toma una string y según su parámetro (espacio por defecto) elimina dichos parámetros del lado derecho de la cadena.

- fptr = open(os.environ['OUTPUT_PATH'], 'w') lo que hace es que con os.environ[] se toman los valores del entorno de desarrollo (environment) y se busca la key OUTPUT_PATH. Eso es algo muy propio de HackerRank y no es común fuera de dicho entorno. Por lo que fuera de HackerRank habría que usar directamente un archivo Ej: fptr = open(archivo.txt, 'w').

- Recordar que al ser fptr un objeto del módulo os, tiene los métodos write() y close().  Siempre hay que usar close() al final.
'''