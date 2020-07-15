# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:22:55 2020

@author: Sriram
"""

# =============================================================================
# Regression
# =============================================================================

# Regression is used to predict target variables(dependent variables) using
# given feature variables(independent variables)

# target - X
# feature - Y

# Predicting sales using discounts given

# X = discounts and Y = sales

# =============================================================================
# Difference between prediction and forecast
# 
# Forcast information is for next week or next month
# Prediction information if for particular function
# =============================================================================

# =============================================================================
# We need to derive an equation in order to predict Y
# 
# The equation will be in the form of 
# 
# Y = W * X + b
# 
# where W = weight(coefficient)
# 
# b = bias(intercept)
# =============================================================================

# There is some assumption which we have to accept before going to
# Regression:

# 1. Linear Relationship X and Y
# 2. X and Y should be multivariate and normally destributed


import pandas as pd
from sklearn import datasets
# from sklearn.preprocessing import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

boston = datasets.load_boston()
boston.DESCR

# X = 13, Y = MEDV, n = 506

X = pd.DataFrame(boston.data,columns = boston.feature_names)
Y = pd.DataFrame(boston.target,columns = ['MEDV'])

X.isnull().sum()
Y.isnull().sum()

# Split the data into train and test

# Train = 70% and Test = 30%

train_x,test_x,train_y,test_y = train_test_split(X,Y,test_size = 0.3,
                                                 random_state = 11)

reg_model = LinearRegression().fit(train_x,train_y)

pred_y = reg_model.predict(test_x)

print(mean_squared_error(test_y,pred_y))

# 21.01 - mean squared error - average error in predicting boston house
# price using delivered equation

print(reg_model.score(train_x,train_y))

# =============================================================================
# R - squared = 0.7321 - percentage variation in target variable 
# expained by derived equation. Higher value is more preffered
# 
# R - squared >= 0.85 - best fit
# R - squared >= 0.7  - good fit
# R - squared <  0.5  - poor fit
# =============================================================================

# Class Assignmemt

loca = 'C:/Users/Sriram/Desktop/Education/Course/Part 2/Class 11/Assignment/'

auction = pd.read_sas(loca + "auction.sas7bdat")

X = auction.iloc[:,1:5]
Y = auction.iloc[:,5]

train_x,test_x,train_y,test_y = train_test_split(X,Y,test_size = 0.3,
                                                 random_state = 10)

reg_model = LinearRegression().fit(train_x,train_y)

pred_y = reg_model.predict(test_x)

print(mean_squared_error(test_y,pred_y))

print(reg_model.score(train_x,train_y))

# R - squared = 0.94 so the Regression is best fit

# Coefficient

print()

print(reg_model.coef_)
print()