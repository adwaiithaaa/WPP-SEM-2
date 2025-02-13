def is_fibo(n):
    a,b=0,1
    while a<=n:
        if a==n:
            return True
        a,b=b,a+b
    return False

def main():
    t = int(input("Enter number of test cases: "))  
    for _ in range(t):
        n = int(input("Enter the number to be checked: "))  
        if is_fibo(n):  
            print("IsFibo")
        else:
            print("IsNotFibo")

main()