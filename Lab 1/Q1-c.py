#(c) The list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter
lst=[]
for i in range(1,27):
        lst.append(chr(96+i)*i)
print(lst)