"""1. Write a program that asks the user to enter a word and then capitalizes every other letter of
that word. So, if the user enters rhinoceros, the program should print rHiNoCeRoS."""

str1=input("Enter the string:")
str2=""
for ch in str1:
    if str1.index(ch)%2!=0:
        newch=ch.upper()
    else:
        newch=ch.lower()
    str2=str2+newch
print(str2)
