# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:31:37 2020

@author: Sriram
"""

# Assignment 22 JAN 2020

# 1

Newlist = ['Rakesh',18.9,23,'Mahesh',356,26.8]

# 2

PersonDetails = ['Mike',[1984, 2017],'Jay',[1979, 2017]]

# 3(i)

Newlist[2]

# 3(ii)

PersonDetails[3][1]

# 3(iii)

Newlist[-2]

# 4

my_list = ['I','L','O','V','E','P','Y','T','H','O','N']

# 4(i)

my_list[2:6]

# 4(ii)

my_list[:3]

# 4(iii)

my_list[5:]

# 4(iv)

print(my_list)

# 4(v)

my_newlist = my_list * 4
my_newlist.__len__()
print(my_newlist)

# __len__() is used to find the lenght of string and lists

# 4(vi)

my_list.index('P')

# 5

evenno = [2,4,7,8,10]
oddno = [1,2,4,6,9]

# 5(i)

evenno[2] = 6

# 5(ii)

oddno[1:4] = [3,5,7]

# 5(iii)

num = evenno
num = evenno + oddno
num.sort()

# 5(iv)

del evenno[1:4]

# del function is used to remove multiple values on the list or string

# 5(v)

evenno = evenno + [12,14,16]
print(evenno)

