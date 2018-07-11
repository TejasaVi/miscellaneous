import math
import os
import random
import re
import sys


complimentary_dict = {
'A': 'T',
'T': 'A',
'C': 'G',
'G': 'C',
}
# Complete the dnaComplement function below.
def dnaComplement(s):
    if s is None:
        return None
    reverse = s[::-1]
    # reverse string
    reverse = list(reverse)
    # take compliment of string
    compliment = ''.join(map(str,[complimentary_dict[item] for item in reverse ]))
    return compliment

if __name__ =='__main__':
    sys.exit(dnaComplement("AGTGC"))
