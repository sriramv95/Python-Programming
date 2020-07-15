# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 08:56:22 2020

@author: Sriram
"""

# =============================================================================
# Linear Regression
# 
# target = numeric
# feature = numeric
# function = LinearRegression
# Accuracy = R - squared
# Error = mean squared error
# =============================================================================

# =============================================================================
# Logistic Regression
# 
# target = binary
# feature = any Value
# function = LogisticRegression
# Model Validation = Confusion Matrix, Accuracy Score and 
# Classification Report
# =============================================================================

# =============================================================================
# Logistic Regression - is used to predict target variable when it is 
# binary,like predicting win/loss of team
# 
# Logistic Regression is in the form of
# 
# logit(P) = weight * X + bias
# 
# where p is the probability of success
# 
# logit(p) = log(p / 1 - p)
# 
# weight = coefficient
# X = feature
# bias = constant or intercept
# =============================================================================

# =============================================================================
# Assumption of the Logistic Regression
# 
# 1. need not to be Linear relation
# 2. need to have normal distribution
# 3. need not to have homoscedascity
# 4. can have multicolinarity
# 5. need to large sample dataset(n>500)
# =============================================================================

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

loca = 'C:/Users/Sriram/Desktop/Education/Course/Part 2/Class 11B/'

titanic = pd.read_csv(loca + 'Titanic.csv')

titanic.shape
titanic.columns
# =============================================================================
# Columns
# 
# ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
#       dtype='object')
# =============================================================================

# =============================================================================
# Data Clearing
# 
# 1. drop isentification variables
# 2. find missing values for each variables
# 3. if the no of missing values is more than 40%, then drop it
# 4. numeric missing values can be replaced by median
# 5. character missing values drop the observations or replace with mode
# 6. convert character variables to numeric variables
# =============================================================================

titanic2 = titanic.drop(['PassengerId','Name','Ticket'],axis = 1) # step 1
titanic2.shape

titanic2.isnull().sum() # Step 2

titanic2.isnull().sum() / len(titanic2) # Step 3
titanic2.drop(['Cabin'],axis = 1,inplace = True) # Step 3

# inplace = True - is used to store result to same location

titanic2 = titanic2.replace(np.nan,titanic2.median()) # step 4
titanic3 = titanic2.dropna(axis = 0) # step 4
titanic3.isnull().sum() # step 4
titanic3.shape # step 4

# convert character variables to dummy variables

titanic3['Sex'].unique() # step 5
titanic3['Embarked'].unique() # step 5

gender = pd.get_dummies(titanic3['Sex'],drop_first = True) # step 6
embark = pd.get_dummies(titanic3['Embarked'],drop_first = True) # step 6

titanic3.drop(['Sex','Embarked'],axis = 1,inplace = True) # step 6

titanic4 = pd.concat([titanic3,gender,embark],axis = 1) # step 6
titanic4.shape # step 6

# Regression Model

X = titanic4.iloc[:,1:]
Y = titanic4.iloc[:,0]

train_x,test_x,train_y,test_y = train_test_split(X,Y,test_size = 0.3,random_state = 10)

Logistic_Model = LogisticRegression().fit(train_x,train_y)

pred_y = Logistic_Model.predict(test_x)

# Model Validation

print(confusion_matrix(test_y,pred_y))
print(accuracy_score(test_y,pred_y))
print(classification_report(test_y,pred_y))

# =============================================================================
# Output
# 
# [[148  21]
#  [ 32  66]]
#
# 0.8014981273408239 - Good fit
#
#               precision    recall  f1-score   support
# 
#            0       0.82      0.88      0.85       169
#            1       0.76      0.67      0.71        98
# 
#     accuracy                           0.80       267
#    macro avg       0.79      0.77      0.78       267
# weighted avg       0.80      0.80      0.80       267
# =============================================================================

