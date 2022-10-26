import matplotlib.pyplot as plt
import numpy as np
x=np.array(['walking','cycling','car','bus','train'])
y=np.array([29,15,35,18,3])
plt.xlabel("Mode of Transport")
plt.ylabel("Frequency")
plt.title("primary mode of transport")
plt.bar(x,y,color="green",width=.1)
plt.show()
