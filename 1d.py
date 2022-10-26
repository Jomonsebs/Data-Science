import numpy as np
d = np.array([[1, 2, 3], [4, 5, 6]] , dtype='complex')
print(d)
print(d.shape)
print(d.ndim)

print(d.reshape(3,2))