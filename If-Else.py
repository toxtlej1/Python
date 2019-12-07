#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
check = {True: "Not Weird", False: "Weird"}
        # True is given the string Not weird
        # False is given the string Weird
print(check[
        n%2==0 and # Will check if n is even or odd. If equal to 0, then it is even
                   # If n has a remainder, then it will be odd. 
        (
            n in range(2,6) # Checking in the inclusive range between 2 and 5
                            # If n is even and in between 2-5, then print Not Weird
            or # Logical comparison operator to check at least one condition is true
            n > 20) # if n isn greater than 20 and is even, then it will be false
                    # printing out Weird. Since False is given the string string Not Weird
    ])