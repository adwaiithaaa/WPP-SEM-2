# 2. PYTHON PROGRAM TO FIND AND CALCULATE THE FACTORIAL OF A NUMBER.
num=int(input("Enter the number: "))
fact=1
while(num>0):
    fact=fact*num
    print(num)
    num=num-1
print("Factorial of the number:",fact)