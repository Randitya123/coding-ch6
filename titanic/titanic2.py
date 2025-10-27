import pandas as pd

reads=pd.read_csv("titanic.csv") 
ad=reads.loc[reads["Age"]<18,"Name"]#conditional selection
pd.set_option("display.max_rows",None)

length=len(ad)
print(length)
#modifying data
reads.iloc[3,2]="uiguiguig"
print(reads.iloc[3,2])
print(reads.columns)
reads.to_csv("titanic2.csv",index=False)
#avgergae of multiple items
print(reads[["Age","Fare"]].mean())
#sorting data
print(reads.sort_values(by="Age",ascending=True).head(10))
