'''3. Write a program that asks the user to enter a length in feet. The program should then give
the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
enter a 2, then the program converts to yards, etc. While this can be done with if statements,
it is much shorter with lists and it is also easier to add new conversions if you use lists.'''
n=int(input("Enter length in feet:"))
lst=['inches','yards','miles','millimeters','centimeters','meters','kilometers']
conversions=[12,1/3,1/5280,304.8,30.48,3.048,0.3048]

print("Enter 1 for conversion to inches")
print("Enter 2 for conversion to yards")
print("Enter 3 for conversion to miles")
print("Enter 4 for conversion to millimeters")
print("Enter 5 for conversion to centimeters")
print("Enter 6 for conversion to meters")
print("Enter 7 for conversion to kilometers")
ch=int(input("Enter choice for conversion:"))
if ((ch>0) & (ch<8)):
    print(n,"Feet is",n*conversions[ch-1],lst[ch-1])
else:
    print("Choice invalid")
        
    
