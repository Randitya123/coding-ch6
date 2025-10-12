import numpy as np
import time
print("speed test")
z=10000000
l1=list(range(z))
#creating an aray
a=np.arange(z)
#time analysis
start=time.time()
l2=[i*2 for i in l1]
end=time.time()
total=end-start
print(total)

#time analysis
start=time.time()
a2=a*2
end=time.time()
total=end-start
print(total)