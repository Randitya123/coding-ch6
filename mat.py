import matplotlib.pyplot as plt 
age=[1,2,3,4,5]
height1=[123,143,163,170,182]
height2=[154,165,180,190,205]
plt.plot(age,height1,"ro-",label="How height increases throughout years")
plt.plot(age,height2,"go-",label="How height increases throughout years")
plt.xlabel("AGE")
plt.ylabel("HEIGHT(CM)")
plt.title("HEIGHT VS AGE")
plt.show()



