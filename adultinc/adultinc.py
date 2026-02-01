import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import scatter_matrix

read=pd.read_csv("adult.csv")
read.columns=["age","org","fnlwgt","edu","edul","marry","prof","fam","race","gender","capg","capl","hr","country","50k"]
#read.rename(columns={"age":"age","org":"org","fnlwgt":"fnlwgt","edu":"edu","edul","marry","prof","fam","race","gender","capg","capl","hr","country","50k"})




print(read.describe())
print(read.info())

#count of missing vlaues
print(read.isnull().sum())
print(read.isin(["?"]).sum())

for i in read.columns:
    print("---%s---" % i)
    print(read[i].value_counts())
#dropping un used data collums
read.drop(["edul","capg","capl","fnlwgt"],axis=1,inplace=True)
print("Unused collums are droped")
inc=set(read["50k"])
print(inc)

read["50k"]=read["50k"].map({" >50K":1," <=50K":0})

print(read.head())
#CONVERTING TEXT DATA TO NUMERICAL DATA
read["gender"]=read["gender"].map({"Male":0,"Female":1}).astype(int)
read["race"]=read["race"].map({"White":0,"Black":1,"Asian-Pac-Islander":2,"Amer-Indian-Eskimo":3,"Other":4,}).astype(int)
read["marry"]=read["marry"].map({"Married-civ-spouse":0,"Never-married":1,"Divorced":2,"Separated":3,"Widowed":4,"Married-spouse-absent":5,"Married-AF-spouse":6,}).astype(int)
read["org"]=read["org"].map({"Private":0,"Self-emp-not-inc":1,"Local-gov":2,"?":3,"State-gov":4,"Self-emp-inc":5,"Federal-gov":6,"Without-pay":7,"Never-worked":8,}).astype(int)
read["prof"]=read["prof"].map({"Prof-specialty":0,"Craft-repair":1,"Exec-managerial":2,"Adm-clerical":3,"Sales":4,"Other-service":5,"Machine-op-inspct":6,"?":7,"Transport-moving":8,"Handlers-cleaners":9,"Farming-fishing":10,"Tech-support":11,"Protective-serv":12,"Priv-house-serv":13,"Armed-Forces":14}).astype(int)
read["fam"]=read["fam"].map({"Husband":0,"Not-in-family":1,"Own-child":2,"Own-child":3,"Unmarried":4,"Wife":5,"Other-relative":6,}).astype(int)

print(read.head())
