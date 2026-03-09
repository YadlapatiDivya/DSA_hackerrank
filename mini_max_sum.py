#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    arr_min = min(arr)
    arr_max = max(arr)
    min_sum = total - arr_min
    max_sum = total - arr_max
    print(max_sum, min_sum)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
