# input: list of values that represent different items of different categories
# output: the total number of pairs that can be made x

import math
import os
import random
import re
import sys

n = 10
lst = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]

def sockMerchant(ar):
    pairs = 0
    un = set(ar)
    for i in un:
        count = ar.count(i)
        if (count % 2) == 0:
            pairs += (count / 2)
        if (count % 2) != 0:
            pairs += (count - 1) / 2
    print(int(pairs))

sockMerchant(lst)