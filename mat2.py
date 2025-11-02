import matplotlib.pyplot as plt 
fruit=["Mango","Banana","Pineapple","Apple","Orange"]
price=[2.50,1.80,2.90,1.50,1.50]
plt.bar(fruit,price,color="red",edgecolor="black",linewidth=3,width=0.5)
plt.title("Fuits and price")
plt.xlabel("Fruit",fontweight="bold",fontsize=12)
plt.ylabel("Price",fontweight="bold",fontsize=12)
plt.show()

month=["JAN","FEB","MAR","APRIL","MAY","JUN"]
rainb=[10,15,20,18,19,19]
raina=[4,6,12,5,6,17]
plt.bar(month,rainb,color="red",edgecolor="black",linewidth=3,width=0.5)
plt.bar(month,raina,color="green",edgecolor="black",linewidth=3,width=0.5)
plt.title("Months and Rain")
plt.xlabel("Month",fontweight="bold",fontsize=12)
plt.ylabel("Rain",fontweight="bold",fontsize=12)
plt.show()


