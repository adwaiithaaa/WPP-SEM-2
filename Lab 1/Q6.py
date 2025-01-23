#6. PYTHON PROGRAM TO REVERSE OF A GIVEN NO.
num=int(input("Enter the number to be reversed:"))
newnum=0
while(num>0):
    rem=num%10
    newnum=newnum*10+rem
    num=num//10
print("The reversed number is:",newnum)