import math
t=int(input("Enter the number of test cases: "))
if (1<=t<=100):
    for i in range(t):
        count=0
        fn=int(input("Enter the first number: "))
        ln=int(input("Enter the last number: "))
        for i in range(fn,ln+1):
            if math.sqrt(i).is_integer():
                count+=1
        print(count)