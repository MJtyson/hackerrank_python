#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    socks_pairs = 0
    set_ar = set(ar)
    for i in set_ar:
        count = ar.count(i)
        if count >= 2:
          socks_pairs += count//2 

    return socks_pairs
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
