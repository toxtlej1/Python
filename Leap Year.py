import sys
import os

def is_leap(year):
    leap = False
    
    # Write your logic here
    # By doing year and modulo 4, it will check if it evenly divides by 4
    # At the same time, it will check if it evenly divides by 400.
    # An or comparison statement is in place incase if a year is does not evenly
    # divide by 100 and returns a remainder. If so, then it is not a leap year. 
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    return leap
# inputtted year is 1990 and going through the statement, it returns a remainder
# Thus, the output will print out false since it does not evenly divide by 100
year = int(raw_input())
print is_leap(year)