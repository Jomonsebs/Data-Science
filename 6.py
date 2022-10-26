import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,1,2,3,],[4,8,6,4]])
print("array",a)
print("exclude 1st row",a[1:4])
print("exclude last column",a[:, 0:3])
print("Display the elements of 1 st and 2 nd column in 2 nd and 3 rd row",a[1:3,0:2])
print("Display the elements of 2 nd and 3 rd column",a[:,1:3])
print("Display 2 nd and 3 rd element of 1 st row",a[0:1,1:3])
v=np.argsort(a)
n=v,a[4:10]
print("Display the elements from indices 4 to 10 in descending order(use–values)",n)