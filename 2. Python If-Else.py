#Pritam Rajak

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    if n >= 2 and n <= 5:
        if n%2==0:
            print "Not Weird"
    if n >= 6 and n <= 20:
        if n%2==0:
            print "Weird"
    if n > 20 :
        if n%2==0:
            print "Not Weird"
    if n%2 != 0:
        print "Weird"
