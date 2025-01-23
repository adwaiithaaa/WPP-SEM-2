#5. PYTHON PROGRAM TO PRINT TABLE OF ANY NO.
num=int(input("Enter the number: "))
fact=0
while(fact<=10):
    prod=num*fact
    print(num,"x",fact,"=",prod)
    fact=fact+1