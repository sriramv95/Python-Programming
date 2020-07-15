# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:04:57 2020

@author: Sriram
"""
# =============================================================================
# Decision tree
# 
# Decision tree is used to predict variable using a tree structure model
# =============================================================================

# =============================================================================
# tree model will be build using two method
# 
# cart model - gini index (gini = sum(p ^ 2,q ^ 2))
# 
# ID3 model - entropy and information gain
# 
# entropy = sum(-p * log2p,-q * log2q)
# 
# information gain - entropy of target - entropy of feature
# =============================================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.metrics import classification_report

loca = 'C:/Users/Sriram/Desktop/Education/Course/Part 2/Class 12/'

balance = pd.read_csv(loca + 'balance_scale.csv')

balance.shape
balance.columns

balance.isnull().sum()

X = balance.iloc[:,1:]
Y = balance.iloc[:,0]

train_x,test_x,train_y,test_y = train_test_split(X,Y,test_size = 0.3,
                                                 random_state = 10)

model_gini = DecisionTreeClassifier(criterion = "gini").fit(train_x,train_y)

pred_y = model_gini.predict(test_x)

print("gini results")

print(confusion_matrix(test_y,pred_y))
print(accuracy_score(test_y,pred_y))
print(classification_report(test_y,pred_y))

# accuracy_score = 0.78 So the model is good fit

# =============================================================================
# Class Assignment
# =============================================================================

# Case 2 class 12

loca1 = 'C:/Users/Sriram/Desktop/Education/Course/Part 2/Class 12/Case Study/Case 2/'

data1 = pd.read_excel(loca1 + 'Data.xlsx')

data1.shape
data1.columns

data1.isnull().sum()

X = data1.iloc[:,-1:]
Y = data1.iloc[:,-1]

# accuracy_score = 1.0 so the model is best fit

# when model accuracy_score = 1 then the model is overfit

import seaborn as sns

sns.heatmap(data1.corr())

# Test portions

# chi square
# signification test - ttest,annova
# regression
# logistic regression