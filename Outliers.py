# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:35:43 2020

@author: Sriram
"""

# =============================================================================
# Outlier - are extremely high or low are called outliers values
# 
# We need to find outliers in the data and replace it with median
# values.In case you left the values as it is will give wrong analysis
# result. Because all analysis uses mean values, which is wrong 
# representation of the mean values in the case of outliers
# =============================================================================

# =============================================================================
# How to find outliers?
# 
# Method 1: Using boxplot method
# 
# high Outlier > Q3 + 1.5 * IQR
# low Outlier > Q1 - 1.5 * IQR
# 
# What is Q3,Q1 and IQR?
# 
# Q3 = Third quartile
# Q1 = First quartile
# IQR = Q3 - Q1
# 
# Method 2: Confidence method (Not Commonly Used)
# 
# mean (+-) 3 * std 
# 
# values above or below is taken as Outlier values
# 
# Outlier Treatement
# 
# Replace the Outlier values with median values
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(10)

# Random sample will be same exicution, so we get same result

array1 = np.random.normal(100,10,200)

# Method 1

plt.boxplot(array1)
box_result = plt.boxplot(array1)
out_value = box_result['fliers'][0].get_data()[1]
out_value
len(out_value) # Displays total number of outliers

# Method 2

out_value = array1[np.abs(array1 - np.mean(array1)) > 3 * np.std(array1)]
out_value

# Outlier Treatement






