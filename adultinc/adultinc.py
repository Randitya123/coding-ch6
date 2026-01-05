import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import scatter_matrix

read=pd.read_csv("adult.csv")
read.columns=["age","org","fnlwgt","edu","edul","marry","prof","fam","race","gender","capg","capl","hr","country","50k"]
print(read.describe())
print(read.info())