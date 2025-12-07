import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
file=pd.read_csv("Data.csv")
x=file.iloc[:,:-1].values
y=file.iloc[:,-1].values
print(x)
print(y)
#mssing data
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy="mean")
imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])
print("After filling mising valuess")
print(x)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
cat=ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[0])],remainder="passthrough")
x=np.array(cat.fit_transform(x))
print("After onehotencoding")
print(x)
from sklearn.preprocessing import LabelEncoder
l=LabelEncoder()
y=l.fit_transform(y)
print("encoded y values")
print(y)
#splitting data into testing and training set
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=1)
print("xtraining data")
print(xtrain)
print("xtest data")
print(xtest)

print("ytraining data")
print(ytrain)
print("ytest data")
print(ytest)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
xtrain[:,1:3:]=sc.fit_transform(xtrain[:, 3:])
xtest[:,1:3:]=sc.transform(xtest[:, 3:])
print(xtrain)
print(xtest)
print("training the machine")
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(xtrain,ytrain)
predictions=classifier.predict(xtest)
print(predictions)
print(ytest)