# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 09:04:14 2020

@author: Sriram
"""

# =============================================================================
# What is a package?
# 
# Packages are compresssed files to store different objects and functions
# =============================================================================

# =============================================================================
# How to import package?
# 
# In order to import a package, we have to use the following procedure
# 
#    import package_name as alias
#    
# This is used to import complete package in the current program. 
# The package should be imported in the every python session
# =============================================================================

# =============================================================================
# To import specific function from a package, we have to use the 'from' keyword
# 
# Syntax:
#     
#     from package_name import function_name
# =============================================================================

import numpy as np

# =============================================================================
# numpy is used for only numeric calculation
# 
# it create an object like matrix which store only similar kind of value
# =============================================================================

data1 = np.array([10,20,30,40,50])
type(data1)
data1.shape

data2 = np.array(np.arange(1,13))
data2
data2.shape

data2.reshape(3,4)
data2.shape
data2

# extraction

data1[2:4]

data2[2,1:3]

# =============================================================================
# Terminology
# 
#  rows - index or observation
#  
#  column - columns or variables
#  
#  table - dataset or dataframe
# =============================================================================
 
# =============================================================================
# Manupilation
# 
# 1. Add
# 
# 2. Delete
# 
# 3. Transpose
# 
# 4. Sort
# 
# 5. Statistical functions
# =============================================================================

# ADD

data3 = np.array(np.arange(2,12))
data3
data3.reshape(2,5)

# SUM

np.add(data3,10)
np.sum(data3)
data3
np.sum(data3,axis = 0)

# DELETE

data1
np.delete(data1,[2])

# TRANSPOSE

np.transpose(data3)

# SORT

data4 = np.array([10,15,12,18,13,17])
np.sort(data4)

# How to sort in descending order

-np.sort(-data4)

# STATISTICAL FUNCTIONS

np.mean(data4)
np.median(data4)
np.var(data4)
np.std(data4)
np.quantile(data4,[0.25,0.5,0.75])

# Random number generation

np.random.randint(10,20,10) # 10 rows and 4 coloumns random values 

np.random.rand(10,20) # 12 normaly distributed data with mean 10 and std 5

np.random.normal(10,5,12) # 12 normally distributed data with mean 10
