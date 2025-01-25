"""Find Digits
You are given a number N, you need to print the number of positions where digits exactly
divides N.
Input format
The first line contains T (number of test cases followed by T lines each containing N).
Constraints
1 <= T <= 15
0 <= N <= 1010
Output Format
For each test case print the number of positions in N where digits in that number exactly
divides the number N in separate line."""

t=int(input("Enter the number of cases:"))
count=0
if (t>=0 and t<=15):
    for i in range(t):
        n=int(input("Enter number:"))
        if (n>=0 and n<=10**10):
            while n>0:
                rem=n%10
                if n%rem==0:
                    count+=1
                n=n//10
            print(count)
            count=0
        else:
            print("Number not valid")
else:
    print("Number of cases more than 15")

                
    
    