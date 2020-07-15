# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 09:54:14 2020

@author: Sriram
"""

# missing value detection and treatment

# =============================================================================
# How to find missing value
# 
# 1. np.isnan(data['varname']).sum() - gives count of missing values
# 2. data.isnull().sum() - gives count of all missing values of all the 
#    variables
# =============================================================================

# =============================================================================
# missing value treatment
# 
# 1. drop missing value
# 2. replace missing value with previous value or next value
# 3. replace missing value with the given value
# 4. replace missing value with median value
# =============================================================================

import numpy as np
import pandas as pd

data = pd.DataFrame(np.random.rand(10,4),columns = list('ABCD'))

# Adding missing values in data

data.iloc[2:3,0] = np.nan
data.iloc[3:6,1] = np.nan
data.iloc[5:9,2] = np.nan

# Display missing values in C

np.isnan(data['C']).sum()

# Missing values in all columns

data.isnull().sum()

# Missing value treatment

# Dropping missing values

data.dropna(axis = 0)

# replace missing value with previous value

data.fillna(method = 'pad')



data.replace(np.nan,1)

# Class assignment

location = "C:/Users/Sriram/Desktop/Education/Course/Part 2/Class 9/"

data1 = pd.read_table(location+ 'pima-indians-diabetes.data.txt',sep = ',',skiprows = 12,header = None)

data1[[1,2,3,4,5]] = data1[[1,2,3,4,5]].replace(0,np.NaN)

data1.isnull().sum()

data1.isnull().sum()/len(data1)

data1[1] = data1[1].fillna(method = 'pad')
data1[2] = data1[2].replace(np.NaN,40)
data1[3] = data1[3].fillna(data1[3].median())
