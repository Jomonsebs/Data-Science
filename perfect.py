print("JOMON SEBASTIAN")
print("21MCA025")
n=int(input("enter the number"))
l=[]
for i in range (1,n):
    if n % i == 0:
        l.append(i)
sum=(sum(l))
if sum==n:
  print("perfect")
else:
    print("not")




