#2. Write a program that generates 100 random integers that are either 0 or 1. Then find the
#longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
#zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.
import random
lst=[]
for i in range(101):
    lst.append(random.randint(0,1))
print(lst)
count=0
lst2=[]
for ele in lst:
    if ele==0:
        count+=1
    else:
        count=0
    lst2.append(count)
print("The longest run of zeroes is:",max(lst2))
    
    