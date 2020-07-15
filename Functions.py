# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 09:19:13 2020

@author: Sriram
"""

# Function 

# Function is used to perform specifi ccalculations and return value

# Syntax for function definition

# def fuction_name(args):
#    python statements
#    return var;

# Note: after first line of function definition, second line will start with a indent,
# do not remove indent.

# Function to add 2 numbers

def total_of_2no(x,y):
    total = x + y
    return total;

total_of_2no(10,20)

total_of_2no(-100,90)

# Functon to find total amount to be paid by the customer, if he get 10% discount

def discount(a,b):
    dis = a * (b / 100)
    famt = a - dis
    return famt;

discount(100,10)

# Scope of a variable

# 1. Local variable: variable created in the funtion 

# 2. Global variable: variable created outside of funtion and you can use it anywhere

def discount(a,b):
    dis = a * (b / 100)
    famt = a - dis
    return famt,dis;

discount(100,10)

# To use global variable in the function

inc = 10

def valueinc(value):
    new = value + value * (inc/100)
    return new;

valueinc(100)

# Function to check the given value is odd or even

def number(num):
    if num % 2 == 0:
        a = 'even'
    else:
        a = 'odd'
    return a;

number(6)
        
# Condition Statements

# 1. if - else statement

# 2. do - while statement

# 3. for statements

# IF Statements 

# Type 1

# if(condition): action 1

# Type 2

# if(condition):
#    action 1
#    action n
# new statement

# Type 3

def f4(num = 0):
    square = 0
    sqrt = 0
    if (0 < num & num < 10):
        square = num * num
        sqrt = num ** (1/2)
    return square,sqrt;

f4(19)
