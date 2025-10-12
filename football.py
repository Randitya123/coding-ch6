import numpy as np
import matplotlib.pyplot as plt
goals=np.array([
    [2,1,0,3,1],
    [0,2,2,1,3],
    [1,2,0,2,1],
    [0,1,0,5,2]
])
#finding mean
mean=np.mean(goals,axis=1)
best=np.argmax(mean)
l1=["a","b","c","d"]
print("AVG goals", mean)
print("Best AVG", l1[best])
#bar graph
plt.bar(l1,mean,color="black")
plt.title("BEST PLAYER")
plt.xlabel("players")
plt.ylabel("goals")
plt.show()