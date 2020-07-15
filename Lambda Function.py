# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 09:06:25 2020

@author: Sriram
"""

# =============================================================================
# lambda function
# =============================================================================

mylist = [10,20,30,40,50]
list1 = [5,5,5,5,5]
newlist = []

# Increament each value of mylist by 5

for i in range(0,len(mylist)):
    newlist.append(mylist[i] + list1[i])
    print(str(newlist))
    
# lambda function - is used to create a temperary function
# Syntax
# f1 = lambda x : x + 5
# f1(10)

# map function - is used to perform calculation to each value of the list using
# lambda function

nlist=list(map(lambda x:x+5,mylist))
print(nlist)

# filter() function - is used tio create a subset from the list

nlist = list(filter(lambda x:x>30,mylist))
print(nlist)

# Class assignment

# Filter the odd numbers from the list into another list

list1 = [1,2,3,4,5,6,7,8,9,0]

nwlist = list(filter(lambda x:x%2!= 0, list1))
print(nwlist)