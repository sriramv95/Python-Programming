# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 08:55:04 2020

@author: Sriram
"""

# =============================================================================
# Flow control statement
# =============================================================================

# if
# while
# for

# while statement is used to execute set of statements while conditions is true

# syntax

# while (condition):
#     python statements1
# else:
#    python statements2
# other statements

time = 9

while(time < 12):
    print("Good Morning")
    time+= 1
else:
    print("Good Afternoon")
    
#write python function to find the number of times i 


def times(num):
    count = 0
    while(num <= 100):
         count+=1
         num+= 10
    return count;

times(50)


# for loop is used to define given set of statements for one time for each value
# in the collection

# for i in the collection:
# python statemnts


for i in [9,10,11,12]:
    print (i)
    print("Good morning")
    
# write python functin to find the value after adding 10 to the user give value 5 times
    
def num(x,tim = 5):
    count = tim
    for i in range(count):
        x+= 10
    return x;

num(50)
num(50,6)

# how to decide which loop we have to use given problem

# Case1 : write python to find the value if I have to save 52/- per week - for loop

def SAV(x):
    count = 0
    for i in range(x, 0, -52):
        count+= 1
    else:
        print("Number of weeks:",count - 1)
        
SAV(10000000)
        
# OR
        
def SAVA(x):
    week = x // 52
    weeks = int(week)
    print("Number of weeks:",weeks)
    
SAVA(1000)

# case 2 : write python function to find the total number of weeks it will take to make 
# 5000

def SAV2(x):
    count = 0
    while x < 5000:
            x = x + 52
            count+= 1
    else:
        print("Number of weeks:",count - 1)
        print("Final x value:",x - 52)

SAV2(0)

# OR

def SAVA(x):
    week = x // 52
    weeks = int(week)
    print("Number of weeks:",weeks)
    
SAVA(5000)

# Flow control statements

# Break
# Continue
# Pass