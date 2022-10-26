import numpy as np
print("1D array")
a=np.array([1,2,3,4])
print(a)
print("insert",np.insert(a,1,10))
print("2D array")
b=np.array([[1,2,3],[4,5,6]])
print(b)
print("insert",np.insert(b,1,5,axis=1))