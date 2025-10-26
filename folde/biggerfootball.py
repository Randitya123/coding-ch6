import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#reading cvs file
csv=pd.read_csv("big_player_goals.csv")
names=csv["Player"]
#dropping player columm
numofgoals=csv.drop("Player",axis=1).to_numpy()
mean=np.mean(numofgoals,axis=1)
best=np.argmax(mean)
print(mean)
print(names[best])
#Plotting the graph
plt.figure(figsize=(12,6))
plt.bar(names,mean,color="blue")
plt.title("AVG Goals the players have scored")
plt.xlabel("PLAYERS")
plt.ylabel("AVG GOALS SCORED")
plt.xticks(rotation=45)
plt.show()
