# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 08:53:21 2020

@author: Sriram
"""

# Pytuhon Test

# 1.

my_list = ["P","Y","T","H","O","N","I","S","B","E","S","T"]

# a.

len(my_list)

# b.

my_list[:8]

# c.

my_new_list = my_list * 3
my_new_list

# d.

my_list.['Y']

# e.

my_list[-3:]


# 2(a).

# =============================================================================
# The difference between List and Tuple is that it is immutable, that is the 
# List values can be edited once it is created whereas in the case of Tuple, 
# it is not editable once created. And list is defined using '[]' brackets and
# tuple is declared by using the '()' brackets.
# =============================================================================

# Example:

sample_list = [1,2,7,4,5]

sample_tuple = (1,2,7,4,5)

# 2(b).

# =============================================================================
# The difference between break and continue statements are that in break statement
# the loop stops at the place where the required condition is met whereas in the 
# continue statement the loop is skipped and moved to the next loop.
# =============================================================================

# Example:

i = 0

if i < 2:
    break
    print(i)

if i < 2:
    print(i)
    continue;
if i < 4:
    print(i)

# 2(c).

# =============================================================================
# The difference between numpy array and pandas dataframe is that in numpy array
# the data is displayed or created in one or more dimensional form whereas in 
# pandas dataframe it is created in the form of tables with appropriate rows and
# columns.
# =============================================================================

# Example:

import numpy as np
import pandas as pd 

np_array = np.array([1,2,3,4,5])   

pd_dataframe = pd.DataFrame('Id':[1,2,3,4,5],
                            'Name':['Ian','Ram','Raju','Ravi','Mohan'])

# 3.

def fact(x):
    while x > 0:
        x-=1
        fac = x * (x-1)
        return fac;

fact(5)

# 4.

def large(x,y,z):
    if(x < y) & ()
    
    
# 5.

x = 0
sum_of = 0

while x <= 10:
    x+= 1
    sum_of = x + x
    
print(sum_of)

# 6. 

X = (23,45,24,123,43,23,32,12,76,8,45)

# 7.

A = np.array([234, 235, 765, 897, 124, 567, 234, 124])
B = np.array([980, 786, 980, 654, 456, 654, 786, 234])

# a.

A[0:4]
B[-4:]

# b.

np.sum(A)
np.product(B)

# e.

A == B

# 9.

First_array = np.array([23, 45, 67, 12, 44],[23, 45, 76, 34, 23])
Second_array = [21, 23, 54, 78, 12][12, 86, 45, 76, 87]
