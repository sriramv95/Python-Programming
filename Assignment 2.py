# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 08:34:19 2020

@author: Sriram
"""

# 1

x = 'Python'
y = 'is'
z = 'best'

# 1a

print(x+y+z)

# 1b

print(x+" "+y+" "+z)

# 1c

print(x*5)

# 1d

print(x[-2:])

# 1e

len(x)

# 2

a = "moon"
b = "moot"
a == b

# 3

print(x.index('o'))
'o' in x

# 4

mylist = [25, 67, 34, 679, 57, 98, 14]

# 4a
mylist.reverse()
print(mylist)

# 4b

mylist.sort()
print(mylist)

# 4c

mylist.insert(0, 789)

# 5

my_tuple = ('Delhi', 'Bangalore', 'Chennai', 'Pune')

# 5a

my_tuple[2][0]

# 5c

my_tuple[3][0]

# 6

my_dict = {'Ajay': 302,'Vijay': 506,'Dheeraj': 786,'Niraj': 931,'Kalyan': 791}

# 6a

my_dict['Niraj']

# 6b

my_dict['Mukesh'] = 625

# 6c

print(my_dict)

# 6d

del my_dict['Vijay']

# 6e

my_dict['Dheeraj'] = 500