import numpy as np
a=np.array([1,2,3])
print(a)
print("Demonstrate the use of diag() function in 1D",np.diag(a))
print("Demonstrate the use of diag() function in 1D",np.diag(a, 1))
print("Demonstrate the use of diag() function in 1D",np.diag(a, -1))
print("2D")
b=np.array([[9,8,7],[6,5,4],[3,2,1]])
print(b)
print("Demonstrate the use of diag() function in 2D",np.diag(b))
print("Demonstrate the use of diag() function in 2D",np.diag(b, 1))
print("Demonstrate the use of diag() function in 2D",np.diag(b, -1))

