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

read["50k"]=read["50k"].map({">50K":1,"<=50K":0})

print(read.head())


