# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:13:47 2020

@author: Sriram
"""

a=100
print(a)

b=a/2
print(b)

a=200
b=a/20
print(b)

name="python"
print("I am learning "+ name)

print("value of a is "+ str(a))

# str() function is used to convert the datatype as string
# "+" is used to concatenate 2 strings

name.upper()
name=name.upper()

# 'name.upper()' function is used to display the string in uppercase
# Every task that we do is a function and every function is called an Object

# Python Programming Part 1

# 1.1 LIST

# List is used to store multiple values of different types as one dimensional array

# we use '[]' to create the list

list1 = [10,20,30,40,50]
list2 = [10,'a',20,'b',30,'c']
print(list1)
print(list2)

list1[1]

# Acessing the second value in the list

list1[2]

# Acessing the second index value in the list

list1[2:4]

# Acessing the second to third index value in the list
# To accesss range of values in the list we need to define one more than the 
# required index value

list1[2:]

# Acessing the second to last index value in the list

list1[:2]

# Acessing from the first till the second index value in the list

list1[2]
list1[2:5]
print(list2[0],list2[-1])

# Used for printing multiple values in list

# Nested List

list3=[[10,20],[30,40],[50,60]]
print(list3)

list3[1][1]

# Used to access values in nested list

list4=[1,[20,30,40],2,[50,60,70]]
print(list4)

# List of even values between 2 to 10

even_no = [2,4,6,8,10]

# OR

Even_no = list(range(2,12,2))
print(Even_no)

# Range function is used to define the frequency of numbers defined in the list
# Range Syntax = range(start,stop,step)

# List Manupulation

pricelist = [100,105,112,115,120]

# To Replace List value

pricelist[2] = 110
pricelist

# To Add new value to the list

pricelist.append(105)
pricelist

# To remove value in the list

pricelist.remove(105)
pricelist

# To insert new value

pricelist.insert(1,107)
pricelist

# To reverse the values o the list

pricelist.reverse()
pricelist

# To sort thevalues in the list

pricelist.sort()
pricelist

# Add 122,128 to pricelist

pricelist = pricelist + [122,128]
pricelist

# To display the index value

pricelist.index(120)
pricelist.extend([122,128])










