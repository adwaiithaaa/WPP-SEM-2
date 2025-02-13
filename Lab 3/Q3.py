def tree(n):
    height=1  
    for ch in range(n):
        if ch % 2 == 0:  
            height=height*2
        else:  
            height=height+1
    return height

def main():
    t=int(input("Enter the number of test cases: "))  
    for _ in range(t):
        n=int(input("Enter the number of cycles: "))  
        print(tree(n))

main()
