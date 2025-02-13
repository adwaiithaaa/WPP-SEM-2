from string import ascii_lowercase
str = input("Enter a sentence: ").lower()
count=0
for char in ascii_lowercase:
    if char not in str:
           count+=1
if count>0:
    print("It is not a pangram")
else:
    print("It is a pangram")

