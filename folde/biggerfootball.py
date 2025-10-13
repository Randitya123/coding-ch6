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