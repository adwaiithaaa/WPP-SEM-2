"""2. Write a program that repeatedly asks the user to enter product names and prices. Store all
of these in a dictionary whose keys are the product names and whose values are the prices.
When the user is done entering products and prices, allow them to repeatedly enter a
product name and print the corresponding price or a message if the product is not in the
dictionary."""

shop={}
ch=input("Do you want to start(Y/N):")
while ch in 'Yy':
    prod=input("Enter the name of the product:").lower()
    price=int(input("Enter the price of the product:"))
    shop[prod]=price
    ch=input("Do you want to continue(Y/N):")
print(shop)
ch2=input("Would you like to search for prices(Y/N):")
while ch2 in "Yy":
    found=False
    search=input("Enter the name of the product to search for:").lower()
    for k,v in shop.items():
        if k==search:
            print("The price of",search,"is",v,"rupees")
            found=True
            break
    if not found:
        print("Product not found")
    ch2=input("Do you want to continue(Y/N):")
    