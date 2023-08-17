#s = input()
#s = sorted(s)
"""s = dict(s)
#print(s)

counts = {}

"""
"""
for k,v in Frequency.most_common(3) :
	print(k,v)"""

"""Frequency = {}
for item in s:
	if item in Frequency :
		Frequency[item] += 1
	else:
		Frequency[item] = 1

#Fre_list = (list(Frequency))
Fre_list = Frequency.most_common(3)

print(Fre_list)

"""

# importing the modules
import math
import os
import random
import re
import sys
from collections import Counter


# using __name__ variable
if __name__ == '__main__':
    
    s = input()
    s = sorted(s)
    
    FREQUENCY = Counter(list(s))
 
    for k, v in FREQUENCY.most_common(3):
        print(k, v)


