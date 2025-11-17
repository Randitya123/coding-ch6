import matplotlib.pyplot as plt

cat=["food","rent","education","worker","electricty","Water","internet","entertainment","miscellaneous","savings"]
exp=[200,1800,4000,150,500,500,250,150,120,1500]
#ploting basic piechart
plt.figure(figsize=(6,7))
plt.pie(exp,labels=cat)
plt.title("Expenses")
plt.show()
#adding colors, shadow and percentage
clr=["red","blue","green","pink","brown","purple","yellow","orange","violet","indigo"]
plt.pie(exp,labels=cat,colors=clr,autopct='%1.1f%%',startangle=90,shadow=True)
plt.title("cool Expenses")
plt.show()
#exploding for highlight
explodinglist=[0,0,0.1,0,0,0,0,0,0,0]
plt.figure(figsize=(8,6))
plt.pie(exp,labels=cat,colors=clr,autopct='%1.1f%%',startangle=90,shadow=True,explode=explodinglist)
plt.title("Expenses")
plt.show()
