# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 09:35:19 2020

@author: Sriram
"""

# 1.2 Data Types

# Python can store 5 different types of values, these are called data types

# Which are as follows:

# 1. Integer: 10, 12, 15

# 2. Float: 10.0, 10.5, 10.9

# 3. String: any value with quotation (' '," ","' '")

# 4. Boolean: True/False

# 5. Complex: a+bj where a = real value b = imaginary value j^2 = -1

i1 = 10

f1 = 10.5

type(i1)
type(f1)

i2 = float(i1)

f2 = int(f1)

print(i2, type(i2))

s1 = 'nikhil'
s2 = 'ANALYTICS'

type(s1)

s1 = s1.upper()
print(s1)

s1 = s1.capitalize()
print(s1)

s1 = s1[:2].upper() + s1[2:]
s3 = s1.capitalize() + " " + s2.capitalize()

s1[0:2] = "NI" # You cannot change the value in the string, string is immutable

x = [10,20]
x[0] = 15
print(x)

# Logical Value

b1 = 10>20

b2 = True

type(b1)

b1 & b2 # b1 and b2 : returns true if both are true

b1 | b2 # b1 or b2 : returns true if anyone is true

# Complex value

c1 = 1 + 2j

c2 = 2 + 3j

type(c1)

print(c1 + c2) # Performing addition for complex values

print(c1 * c2) # Performing multiplication for complex values

# In order to store multiple values, we need following object

# LIST - [] is mutable

# TUPLE - () is immutable 

# DICTIONARY - {} - is mutable, store values in key:value pair

my_tuple = (10,20,30)

my_tuple[1] = 25 # Error 'Tuple is immutable'

my_dic = {'a':10,'b':20,'c':30}
my_dic['b']

# To know all the values

my_dic.values()

# to add new value and replace value and remove value

my_dic['d'] = 40
my_dic['d'] = 50
del my_dic['b']

# To know all the keys

my_dic.keys()

# keys with two values

my_dic['e'] = [40,50]
