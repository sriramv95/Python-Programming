# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:51:20 2020

@author: Sriram
"""

import numpy as np

import pandas as pd

from scipy.stats import chi2_contingency

Path = "C:/Users/Sriram/Desktop/Education/Course/Part 2/Class 10/"

tooth = pd.read_csv(Path + "tooth_growth.csv")

tooth_pivot = pd.pivot_table(tooth, values = ['len'], index = ['supp'],
                            columns = ['dose'], aggfunc = np.sum)

tooth_final = tooth_pivot.replace(np.NaN,0)

chsq, pvalue, dof, exp = chi2_contingency(tooth_final)
