import matplotlib.pyplot as plt
import numpy as np

x= np.array([2001,2002,2003,2004,2005,2006,2007])
y = np.array([24000,22500,19700,17500,14500,10000,5800])
plt.xlabel('YEAR',color="red")
plt.ylabel("CAR VALUE",color="red")
plt.grid()
plt.title("Value Depreciation",loc="left",color="red")
plt.plot(x, y,color="red",linestyle="dashdot",marker="*",markerfacecolor="green",markersize=20)
plt.show()