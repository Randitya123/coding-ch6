import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5]
y=[1,2,3,4,5]

plt.plot(x,y,"ro-")
plt.show()
#comparing multiple graphs
plt.plot([1,2,3,4,5],[1,4,9,16,25],"bo-",label="y=x^2",linewidth=5)
plt.plot([1,2,3,4,5],[1,8,27,64,125],"go-",label="y=x^3",linewidth=5)
plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
plt.axis([0,5,0,30])

plt.title(".")
plt.legend()
plt.show()
#user input graph
m=float(input("Enter the value of slope"))
c=float(input("Enter the value of constant"))

x=np.arange(0,10,0.1)
y=m*x+c
plt.plot(x,y,"ro-",label=f"y={m}x+{c}",linewidth=5)
plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
plt.legend()
plt.grid(True)
plt.show()

