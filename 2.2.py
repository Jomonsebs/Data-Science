import numpy as np
b=np.array([[1,2,3],[6,5,4],[3,2,1]])
c=np.array([[1,5,3],[7,5,4],[3,2,1]])
print(b)
print("cube",np.power(b,3))
c=np.multiply(b,b)
print("multiply cube",np.multiply(c,b))
print("using *",b*b*b)
print("using **",b**3)
print("identity",np.identity(3,dtype=int))
h=np.multiply(b,b)
print("h",h)
j=np.add(c,c)
print("j",j)
k=np.add(h,j)
print("x2+2y",k)






