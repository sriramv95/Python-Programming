# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 06:48:03 2020

@author: Sriram
"""

# =============================================================================
# Assignment 3
# =============================================================================

# 1. To accept two numbers X and Y and find the sum of it.

def SUM(x,y):
    total = x + y
    return total;

SUM(67,56)

# 2. To solve the equation f(x) = ax2 + bx + c. By passing x value and a = 2, 
# b = 4 and c = 9

def quad(a,b,c,x):
    eq = (a * x ** 2) + (b * x) + c
    return eq;

quad(2,4,9,2)

# 3. To pass three arguments Principal, Rate of Interest & Time and calculate 
# the Simple Interest.

def INT(p,r,t):
    SI = p * r * t / 100
    return SI;

INT(20000,8,25)

# 4. To calculate the square root of a number.

def SQRT(x):
    root = x ** (1/2)
    return root;

SQRT(4)

# 5. To find final amount that needs to be paid by customer based on given 
# quantity and price. Add GST 18% and subtract discount of 12% to get final 
# amount

def GST(x):
    tax = x * (18 / 100)
    dis = x * (12 / 100)
    fin_amt = x + tax - dis
    return fin_amt;

GST(2500)

# 6. To returns the square of the sum of two numbers X and Y i.e. (X+Y)2

def SUM2(x,y):
    eqn = x ** 2 + (2 * x * y) + y ** 2
    return eqn;

SUM2(2, 4)

# 7. To returns the square of the sum of two numbers X and Y i.e. (X+Y)2, where
# default value of the second argument(Y) is 2

def SUM3(x,y):
    eqn = x ** 2 + (2 * x *y) + y ** 2
    return eqn;

SUM3(3,4)

# 8. To convert first and last character of given name into lowercase and rest 
# should be in uppercase

def LOW(name):
    up = name.upper()
    low = up[0].lower() + up[1:-1] + up[-1].lower()
    return up,low;

LOW("sriram")

# 9. To get h in a right angled triangle, where default value of p and b are 3 
# and 4 respectively

def TRI(p,b):
    h = (p * p + b * b) ** (1/2)
    return h;

TRI(3,4)

# 10. To pass an argument containing a word and returning the word by adding 
# ‘ing’ at the end.

def SUF(word):
    fin = word + "ing"
    return fin;

SUF("comm")