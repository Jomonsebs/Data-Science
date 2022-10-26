print("febonacci number")
nterm = int(input("enter a value"))
n1 = 0
n2 = 1
count = 0
for i in range(nterm):
 if( nterm < 0 ):
    print("negative values cannot be applied")
 elif( nterm == 1 ):
    print("the febonacci number is :",nterm)
 else:
    
    nth = n1 + n2
    n1 = n2
    n2 = nth


    print(nth)


