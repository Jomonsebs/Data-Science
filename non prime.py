print("JOMON SEBASTIAN")
print("21MCA025")
n=int(input("enter the limit"))
n1=int(input("enter the second limit"))
for i in range(n,n1):
    for j in range(2,i):
        if i % j == 0:
            print(i)
            break
