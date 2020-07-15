# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:12:03 2020

@author: Sriram
"""

# =============================================================================
# Chi Square Analysis
# 
# Test association between two categorical variables
# 
# Examples: Age, Grade, Genres
# =============================================================================

# =============================================================================
# Chi Square Analysis is done by below formula
# 
# xsq = sum((expected - observed) ^ 2 / expected)
# 
# expected = Row total * Column total / total observations
# =============================================================================

# =============================================================================
# Chi Square Assumption
# 
# H0 = there is no association between given variables
# H1 = there is association between given variables
# =============================================================================

# Reject H0 when pvalue is below 0.05 and accept H1 that means
# given variables has association

# =============================================================================
# dof = degree of freedom
# dof = (r - 1) * (c - 1)
# r = no of rows of contigency tables
# c = no of Columns of contigency tables
# =============================================================================

# contigency tables: is cross table of given variables

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

Path = "C:/Users/Sriram/Desktop/Education/Course/Part 2/Class 10/"

hair = pd.read_table(Path+"hair_eye_color.txt",
                     delim_whitespace = True, header = 0)

cont_table = pd.pivot_table(hair, values = ['n'], index = ['Hair'],
                            columns = ['Eye'], aggfunc = np.sum)

table = cont_table.replace(np.NaN,0)

chsq, pvalue, dof, exp = chi2_contingency(table)

