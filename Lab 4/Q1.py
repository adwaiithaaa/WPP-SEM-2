
t = int(input("Enter the number of test cases: "))

if (1 <= t <= 10):
    for ch in range(t):
        s = input("Enter the string: ").lower()
        count = 0
        left=0
        right=len(s) - 1

        while left < right:
            count += abs(ord(s[left]) - ord(s[right])) 
            left += 1
            right -= 1

        print(count)


        
                
            
    
    
