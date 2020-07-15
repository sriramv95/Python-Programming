# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:13:27 2020

@author: Sriram
"""

# =============================================================================
# Significance Test
# =============================================================================

# =============================================================================
# Significance Test : is used to test or assumption related to population
# from given sample. Assumption will be related to mean(average) value of
# population.
# 
# H0(null hypothesis) = is our assumption
# H1(Alternate hypothesis) = is opposite of our assumption
# =============================================================================

# To test our assumption, we need a sample data with their age value

sample = [40,24,33,39,38,33]

import numpy as np

xbar = np.mean(sample);xbar
s = np.std(sample)
stderror = s / np.sqrt(len(sample) - 1)
assumed_mean = 30
t = (xbar - assumed_mean) / stderror
df = len(sample) - 1

from scipy import stats

stats.t.ppf(1 - 0.05, df) #2.015048372669157

# As t value is 1.85 which is below the critical value 2.015, so we 
# accept our assumption. That is the mean value is 30

stats.ttest_1samp(sample,30)

# statistic=1.8500095165343353, pvalue=0.12354721380516265

# if t - statistics is less than t - value from table then accept your
# assumption(H0) or pvalue is more than 0.05, then accept H0 (this method
# we always use)

# =============================================================================
# TTest - is used to compare assumed population mean with sample mean
# value. There are 2 types of ttest:
#     
#     1 sample ttest
#     
#     ttest_1samp() - H0: population_mean = value,
#                     H1: population_mean not = value
#     
#     2 sample ttest
#     
#     ttest_ind()
#     
#     (a) Unpaired ttest = H0 mean_1 = mean_2
#     H1 = mean_1 not = mean_2
#     
#     (b) Paired ttest = H0: before_mean - after_mean = 0
#     H1: before_mean - after_mean not = 0
# =============================================================================
      
import pandas as pd
from scipy import stats

location = "C:/Users/Sriram/Desktop/Education/Course/Part 2/Class 10/"
wage_data = pd.read_table(location + "wage.txt", skiprows = 26, header = None,
                          skipfooter = 6)

wage_data.shape
wage_data.columns

# average wage is 15
# H0 = 15
# H1 not = 15

stats.ttest_1samp(wage_data[5],15)
# statistic=-26.871368673259415, pvalue=3.432186039340737e-101

# =============================================================================
# Conclusion:
# 
# as pvalue is less than 0.05, so we reject the H0 and accept H1
# this mean average wage is not equal to 15, and as T - statistics is 
# less than 0(-ve), we need to assume more higher value actual value
# =============================================================================

stats.ttest_1samp(wage_data[5],9)
# statistic=0.10820459315650764, pvalue=0.9138741216086457

# =============================================================================
# Conclusion:
# 
# as pvalue is greater than 0.05, so reject the H1 and accept H0
# this means the average wage is not equal to 9, and as T - statistics 
# is more than 0(+ve),we need to assume more lower value than actual 
# value.
# =============================================================================

# (ii) Whether the gender gap is usuage

female_wage = wage_data[wage_data[2] == 1][5]
male_wage = wage_data[wage_data[2] == 0][5]

# H0: female_wage = male_wage
# H1: female_wage != male_wage

stats.ttest_ind(female_wage,male_wage)

# statistic=-4.840066806168903, pvalue=1.7032659492725048e-06

# =============================================================================
# Conclusion:
#     
#     as pvalue is less than 0.05, so we reject H0, that means female
#     wage is not equal to male wage
# =============================================================================

# When we have more than two groups, then we use anova to compare group
# mean value

# Whether different occupation have same average wage

manage_wage = wage_data[wage_data[8] == 1][5]
sales_wage = wage_data[wage_data[8] == 2][5]
clerical_wage = wage_data[wage_data[8] == 3][5]
service_wage = wage_data[wage_data[8] == 4][5]
pro_wage = wage_data[wage_data[8] == 5][5]
other_wage = wage_data[wage_data[8] == 6][5]

# H0: different occupation have the same average age
# H1: different occupation do not have the same average age

# =============================================================================
# Anova Test
# =============================================================================

stats.f_oneway(manage_wage,sales_wage,clerical_wage,service_wage,
               pro_wage,other_wage)

# statistic=23.223918389002986, pvalue=4.1217420634431825e-21

# =============================================================================
# Conclusion:
#     
#     as pvalue is less than 0.05 so we reject H0, then means different
#     occupation have different average wage
# =============================================================================

wage_data.groupby(by = 8)[5].mean()

# Management and professional have higher wages

# Paired TTEST

before_staying_in_south_wage = wage_data[wage_data[1] == 1][5]
after_staying_in_south_wage = wage_data[wage_data[1] == 0][5][:156]

stats.ttest_rel(before_staying_in_south_wage,after_staying_in_south_wage)

# statistic=-3.5958453361560885, pvalue=0.00043412138199877803

# =============================================================================
# Conclusion:
#     
#     pvalue is less than 0.05 so we reject H0
#     before_staying_in_south_wage is not equal to after_staying_in_south_wage
# =============================================================================

# Class Assignment 

