# input: string of steps, either U (+1) or D (-1)
# output: return an integer that denotes the number of valleys

import math
import os
import random
import re
import sys

def countingValleys(n, s):
    seaLevel = 0
    valleys = 0
    inValley = False

    for i in s:
        if i == 'U':
            seaLevel += 1
        if i == 'D':
            seaLevel -= 1
        if seaLevel < 0:
            inValley = True
        if seaLevel == 0  and inValley == True:
            inValley = False
            valleys += 1
    print(valleys)

# test 
numSteps = 8
steps = 'UDDDUDUU'


countingValleys(numSteps, steps)
