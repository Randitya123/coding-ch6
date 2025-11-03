import matplotlib.pyplot as plt
study=[1,2,3,4,5,6,7,8,9,10]
numofmarks=[10,20,30,40,50,60,70,80,90,100]
#plotting scatter plot
plt.scatter(study,numofmarks,color="blue",s=67,marker="*",edgecolor="blue")
plt.title("How the number of hours studied affects the amount fo marks you get?")
plt.xlabel("Study")
plt.ylabel("Marks")
plt.grid(True)
plt.show()