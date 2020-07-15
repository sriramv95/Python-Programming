# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 08:58:28 2020

@author: Sriram
"""

import pandas as pd

loca = 'C:/Users/Sriram/Desktop/Education/Course/Part 2/Class 11B/Logistic regression/Case1/'

adult = pd.read_csv(loca + 'adult.csv')
bank = pd.read_csv(loca + 'bank.csv')

bank.columns
bank.shape

Bank Databas