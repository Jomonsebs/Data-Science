import numpy as np
b=np.random.randint(10,20,size=(2,2))
print(b)
print("inverse",np.linalg.inv(b))
print("rank",np.linalg.matrix_rank(b))
print("determinant",np.linalg.det(b))
print("reshape 1D",b.reshape([1,4]))
e_vector=np.linalg.eig(b)
e_value=np.linalg.eig(b)
print("vector is",e_vector)
print("values",e_vector)


