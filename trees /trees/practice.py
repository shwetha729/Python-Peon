#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findNumber' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#

def findNumber(arr, k):
    # Write your code here
    yes = "YES"
    no = "NO"

    for n in arr:
        if n is k:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5]
    k = 1

    findNumber(arr, k)
