def max_xor(L, R):
    maxval = 0
    for i in range(L, R + 1):
        for j in range(i, R + 1): 
            maxval = max(maxval, i^j)
    return maxval
L = int(input("Enter min : "))
R = int(input("Enter max : "))
print(max_xor(L, R))