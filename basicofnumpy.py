import numpy as np

#1d array
ar=np.array([1,2,3,4,5])
print(ar)

#2d array
dt=np.array([
    [1,2,3,4,5],
    ["a","b","c","d","e"]
    ])
print(dt)

zeros=np.zeros((4,4))
print(zeros)

ones=np.ones((6,7))
print(ones)

six=np.full((5,5),6)
print(six)

#basic math operations with arrays
ar=np.array([1,2,3,4,5])
r=np.array([6,7,8,9,10])

print("Addition", ar+r)
print("multi", ar*r)
print("sub", ar-r)
print("div", ar/r)

#built in numpy math
a=np.array([25,276,12,8,456])
sq=np.sqrt(a)
print(sq)

mean=np.mean(a)
print(mean)

su=np.sum(a)
print(su)

maxnum=np.max(a)
print(maxnum)

minnum=np.min(a)
print(minnum)
