# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:03:54 2020

@author: Sriram
"""

# Correlation is used to find the relation between 2 numeric variables, such as
# height and weight, price and qty, discount and qty.

# =============================================================================
# Correlation is measured by Correlation Coeffiecient(r)
# r between x and y = covariance between x and y / std of x * std of y
# covariance between x and y = sum((xi - xbar)*(yi - ybar))/(n - 1)
# xi = ith value of x, xbar = mean of x
# yi = ith value of y, ybar = mean of y
# =============================================================================

# =============================================================================
# value of r lies between -1 and 1
# 
# -ve value = negative Correlation - means if one variables increase othe will 
# decrease or vice versa
# 
# +ve value = positive Correlation - means both variables increase or decrease 
# together
# 
# Zero value = no Correlation
# =============================================================================

# =============================================================================
# Types of Correlation
# 
# if absolute value of r:
#     0 - 0.3 - weak Correlation
#     0.3 - 0.5 - moderate Correlation
#     0.5 - 1 - strong Correlation
# =============================================================================
    
# =============================================================================
# Correlation test
# 
# H0 = (Null Hypothesis) - Correlation is equal to Zero
# 
# H1 = (Alternate Hypothesis) = Correlation is not equal to Zero
# =============================================================================

# pvalue >= 0.5, we accept h0, else reject h0
# Rejecting the h0 means we accept H1
# 0.5 is called the significance level, that is if we perform test with 100 
# samples, then 5% of the sample will be different from 95% of the sample.

# =============================================================================
# To Calculate pvalue
# 
# z = (x - mean) / std
# p(z) = this comes from z table 
# pvalue = 1 - p(z)
# =============================================================================

import numpy as np
from scipy.stats import pearsonr
import pandas as pd
import matplotlib.pyplot as plt

x = [180,165,157,162,175,153,178,177]
y = [82,52,53,55,80,51,84,100]
dataf = pd.DataFrame({'x':x,'y':y})

dataf['x'].corr(dataf['y']) # Correlation value

dataf.corr() # Correlation matrix

np.corrcoef(x,y) # Numpy correlation code

pearsonr(x,y) # Pearson correlation code

plt.scatter(x,y) # plotting the correlation values

# =============================================================================
# (0.8913930866624139, 0.0029474640292817887)
# (Correlation value, pvalue)
# =============================================================================

# Conclusion - there is +ve strong correlation between x and y. as pvalue is less
# than 0.05, so we reject H0, this means correlation is not equal to Zero

data1 = pd.read_excel("Data.xlsx")

data1.columns

data1['MPG'].corr(data1['WEIGHT'])

data1.corr()

plt.scatter(data1['MPG'],data1['WEIGHT'])
