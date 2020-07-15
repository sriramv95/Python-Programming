# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 09:30:45 2020

@author: Sriram
"""

# =============================================================================
# Extraction of data into python from different source
# =============================================================================

import pandas as pd
import os

# Set Working directory & viewing the files

os.chdir("C:/Users/Sriram/Desktop/Education/Course/Part 2/Class 7/Assignments")
os.listdir()

# Extraction from text file - pd.read_table()

data1 = pd.read_table("company.txt",sep = "/",header = None)
data1.shape

# Extraction from csv file

data2 = pd.read_csv("crabtag.csv")
data2.shape

# Extraction from excel file

data3 = pd.read_excel("sales.xlsx")

# Extration from SAS file

data4 = pd.read_sas("cars.sas7bdat")

# How to read sheet 2 data from excel file

data3a = pd.read_excel("sales.xlsx",sheet_name = "Sheet1")

# Extraction of data from database file
# sql server,oracle,teradata,mysql,nosql,mangodb etc

import pyodbc

conn = pyodbc.connect(dsn = 'python')
data5 = pd.read_sql('select * from spt_monitor',conn)
data5
