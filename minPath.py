import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0

    try:

        for i, cloud in enumerate(c):
            while i < len(c):
                if c[i + 1] == 1:
                    jumps += 1
                    i += 2

                if c[i + 1] == 0 and i + 2 >= len(c) :
                    jumps += 1
                    i += 1

                if c[i + 1] == 0 and c[i +2 ] == 0:
                    jumps += 1
                    i += 2

                if c[i + 1] == 0 and c[i + 2] == 1:
                    jumps += 1
                    i += 1
    except:
        pass
    return jumps

# test 
c1 = [0, 0, 1, 0,0, 1, 0]
c2 = [0, 0, 0, 0, 1, 0]
c3 = [0, 0, 0, 1, 0, 0]

j1 = jumpingOnClouds(c1)
print(j1)
j2 = jumpingOnClouds(c2)
print(j2)
j = jumpingOnClouds(c3)
print(j)