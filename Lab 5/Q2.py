def cuts(k):
    half = k // 2
    return(half*(k-half))

n = int(input("Enter number of test cases: "))
for i in range(n):
    num_cuts = int(input("Enter the maximum number of cuts to make: "))  
    print(f"Maximum number of pieces that can be made with {num_cuts} cuts is {cuts(num_cuts)}")
