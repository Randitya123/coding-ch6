import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix
read=pd.read_csv("iris.csv")
print(read.head())
print(read.info())
#data preprocessing
read['species']=read['species'].replace({"setosa":0,"versicolor":1,"virginica":2})
#visualizing the data
plt.subplot(221)
plt.scatter(read["petal_length"],read["species"],s=10,c="red",marker="o")
plt.title("Petal length vs species")
plt.subplot(222)
plt.scatter(read["petal_width"],read["species"],s=10,c="blue",marker="o")
plt.title("Petal width vs species")
plt.subplot(223)
plt.scatter(read["sepal_length"],read["species"],s=10,c="green",marker="o")
plt.title("Sepal length vs species")
plt.subplot(224)
plt.scatter(read["sepal_width"],read["species"],s=10,c="yellow",marker="o")
plt.title("Sepal width vs species")
plt.tight_layout()
plt.show()
#testing and training
y=read["species"]
x=read.drop("species",axis=1)
print(x.head())
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=1)
print(xtrain.shape)
print(xtest.shape)
model=DecisionTreeClassifier(max_depth=3,random_state=1)
model.fit(xtrain,ytrain)
#predicting
preds=model.predict(xtest)
#checking accuracy
print("accuracy",round(metrics.accuracy_score(preds,ytest),2))
print("accuracy percentage",round(metrics.accuracy_score(preds,ytest)*100,2),"%")
print(preds)
print(ytest)
#confusiojn matrix
values=confusion_matrix(ytest,preds)
print(values)
plt.imshow(values,cmap="Blues")
plt.title("Heatmap")
plt.colorbar()
plt.xlabel("PREDICTED VALUES")
plt.ylabel("ACC DATA")
plt.show()
