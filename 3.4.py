import matplotlib.pyplot as plt
import numpy as np
x=np.array(['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'])
y=np.array([173,153,195,147,120,144,148,109,174,130,172,131])
plt.plot(x,y,color="pink",linestyle="-")
plt.xlabel("Months of Year with font size 18")
plt.ylabel("Sales of Segments")
plt.title("Sales Data")
z=np.array([189,189,105,112,173,109,151,197,174,145,177,161])
plt.plot(x,z,color="yellow",linestyle="solid")

k=np.array([185,185,126,134,196,153,112,133,200,145,167,110])
plt.plot(x,k,color="blue",linestyle=":")
plt.legend(["pink","yellow","blue"],loc="upper right")
plt.show()