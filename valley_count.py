import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys():
        s = list(input('Enter U if Gary goes up/ D if Gary goes dawn: '))#Uphill or dawnhill direction
        n = len(s)#number of step maken
        valley_count = 0
        line = 0
  
        print(s)
        print(n)

        for i in s:
            if i == 'U':
                line += 1
            else:
                line -= 1

        if line == 0 and i == 'U':
            valley_count += 1

                
        print(valley_count)
        print(line)
                        
countingValleys()

