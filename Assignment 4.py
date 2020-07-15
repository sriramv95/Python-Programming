# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 21:26:54 2020

@author: Sriram
"""

# =============================================================================
# ASSIGNMENT 4
# =============================================================================

# Find the sum of all the numbers stored in a list.

num = [1,2,3,4,5,6,7,8,9]
sum1 = 0

for i in num:
    sum1 = sum1 + i
    
print("The sum is",sum1)

count = 0

# Check if a number is positive, negative or zero.

def posneg0(x):
    if x > 0:
        print("Positive")
    elif x == 0:
        print("Zero")
    elif x < 0:
        print("Negative")
        
posneg0(-1)

# Check greatest number among three numbers.

def largest(x,y,z):
    if (x > y) and (x > z):
        largest_num = x
    elif (y > x) and (y > z):
        largest_num = y
    else:
        largest_num = z
    print("The largest of the 3 numbers is : ", largest_num)
    
largest(12, 25, 37)

# Find the sum of first 10 natural numbers using while loop. (sum = 1 + 2 + 3 + ……. + 10)
        
sum2 = 0

for i in range(1,11,1):
    sum2 = sum2 + i
    
print("The sum of first 10 natural numbers is:",sum2)
      
        
        
        
        