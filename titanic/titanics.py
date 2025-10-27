import pandas as pd
#dataframe
df=pd.DataFrame({
    "NAME":["John","Mike","Adam"],
    "CITY":["Mumbai","Zurich","Sao Paulo"],
    "AGE":[3,90,67]
})
print(df)
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
#titanic data set
reads=pd.read_csv("titanic.csv")
print(reads)
print(reads.head())
print(reads.shape)
print(reads.info())
print(reads.describe())
mfc=reads[(reads["Sex"]=="male") & (reads["Pclass"]==1)]
print(mfc["Fare"].mean())

#grouping and anaylisis

holdata=reads.groupby("Pclass")["Fare"].mean()
print(holdata)

holdata=reads.groupby("Name")["Survived"].mean()
print(holdata)
