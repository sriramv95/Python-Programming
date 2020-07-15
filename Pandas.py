# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:11:09 2020

@author: Sriram
"""

# =============================================================================
# Pandas package - is used to general task such as storing data is in the form of
# a table, sorting of data, by group calculation etc.ArithmeticError
# 
# All sorts of basic exploration data analysis(EDA) will be performed by Pandas
# package. In order to use pandas package, we need to install it first, then
# import in every session.
# =============================================================================

import pandas as pd

# =============================================================================
# Pandas has 2 types: Series and Dataframe
# 
# Series - is used to store similar types of values and it is one dimentional 
# array
# 
# Dataframe - is used to store different types of values in a spreadsheet format,
# it is a 2 dimentional array
# =============================================================================

sr = pd.Series([1,2,3,4,5])
print(type(sr))
print(sr)

data1 = pd.DataFrame({'x':[101,102,103,104],
                      'y':['a','b','c','d'],
                      'z':['M','F','M','F']
                      })

print(type(data1))
print(data1)

# Note: Each column should have equal number of values

data2 = pd.DataFrame({'x':[100,101,102,103],
                      'y':'blr',
                      'z':'India'})

print(data2)

data3 = pd.DataFrame({'x1': [100,101,102,103],
                      'x2': ['blr','chn'] * 2,
                      'x3': ['India'] * 4})

print(data3)

import numpy as np

# For Data with missing values

data4 = pd.DataFrame({'x':[100,101,102,103],
                      'y':['blr',np.nan,'chn','mum'],
                      'z':['India'] * 4})

print(data4)

# Class Assignment

data5 = pd.DataFrame({'id':['A101','A102','A103','A104','A105','A106','A107',
                            'A108','A109','A110'],
                      'Name':['Ravi','Mona','Rabina','Mohan','Ganesh','Raju',
                              'Roja','Ramesh','Himani','Manish'],
                      'Sex':['M','F','F','M','M','M','F','M','F','M'],
                      'Age':np.random.randint(20,40,10),
                      'Salary':[25000,35000] * 5})

print(data5)

# Extraction

data5['Name']

data5['Name'][0:5]

data5[['Name','Age']]

data5[0:5]

# What is the salary for mohan

data5[data5['Name'] == 'Mohan']['Salary']

# What is the salary for mohan and ganesh

print(data5[data5['Name'] == 'Mohan']['Salary']
data5[data5['Name'] == 'Ganesh']['Salary'])

# basic information about DataFrame

print(data5.head())
print(data5.tail())
print(data5.shape)
print(data5.columns)

# dataframe manupilation

# addind new column

data5['HRA'] = data5['Salary'] * 0.3
print(data5)

# dropping coloums

data5.drop(['id'],axis = 1,inplace = True)

# axis = 1 means column delete
# inplace = True means same result to same data frame

# Transpose the data

data5.T

# Sorting the data frame

data5.sort_values(by = 'Salary')

# Grouping by calculation 

# Find the average 

# Sum of HRA column

data5.groupby(by = 'Sex')['Salary'].mean()

data5.groupby(by = 'Sex')['HRA'].mean()

data5['HRA'].sum()






