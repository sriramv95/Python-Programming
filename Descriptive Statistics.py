# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 09:16:14 2020

@author: Sriram
"""

# =============================================================================
# Descriptive Statistics
# =============================================================================

# is used to find how the given data is distributed and various statistical 
# values

# =============================================================================
# it is defined in 4 terms:
#     
#     1. Central Tendancy
#     2. Dispersion
#     3. skewness
#     4. kurtosis
#     
#  Mean: it is the average value. sum of all values / no of values
#  
#  median: It is middle most values after sorting the data in descending order
#  
#  mode: it is the frequently occuring value in the data
# =============================================================================

import pandas as pd
import os

os.chdir("C:/Users/Sriram/Desktop/Education/Course/Part 2/Class 7/Assignments")
os.listdir()

data1 = pd.read_excel('sales.xlsx')
data1.shape
data1.columns

data1['Sales'].mean()
data1.median()
data1.mode()

# =============================================================================
# Variance: average deviation from mean value 
# 
# Standard Deviation: square root of average deviation
# 
# Range: Difference between max and min values
# 
# IQR: Difference between Q3 and Q1 values
# 
# Q3: 3rd quartile values
# Q1: 1st quartile values
# 
# Quartile means dividing the data in to 4 equal parts after sorting it.ArithmeticError
# 
# First 25% data: Q1
# Second 25% data: Q2
# Third 25% data: Q3
# =============================================================================

# =============================================================================
# Why do we need to calculate mean, median and mode?
# 
# This will help us to identify or potential customer or target
# if a new customer/client comes whos age is close to average age of your right:
# customer, then you can put extra effort to make him buy from you
# =============================================================================

data1.std() # Standard Deviation
data1.var() # Variance

data1['Sales'].max() - data1['Sales'].min() # Range

data1.quantile([0.25,0.5,0.75]) # Quartile values

# =============================================================================
# Why we need this?
# 
# this will help us to find customer range my customer needs varies, and help us
# to understand their requirement
# =============================================================================

# =============================================================================
# skewness - defines spreadness of data along with the mean.
#
# +ve skewness - when we have more observations below mean
# -ve skewness - when we have more observations above mean
# 0 skewness - equal number of observations to mean
# =============================================================================

data1.skew()

# =============================================================================
# Kurtosis - defines peak of graph at mean value
# 
# 0 kurtosis - Peakness of graph is equal to normal distribution
# -ve kurtosis - Peakness of graph is less than normal distribution
# +ve kurtosis - Peakness of graph is more than normal distribution
# =============================================================================

data1.kurt()

import seaborn as sns # Seaborn module is used for data visualization

sns.distplot(data1['Sales'],hist = True,kde = True) # Histogram
