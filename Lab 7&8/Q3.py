class Bank:
    def __init__(self):
        self.accs = {}  

    def create_acc(self, name, bal=0):
        if name not in self.accs:
            self.accs[name] = bal  
            print(f"Account for {name} created with balance {bal}.")
        else:
            print(f"Account for {name} already exists.")

    def deposit(self, name, amt):
        if name in self.accs and amt > 0:
            self.accs[name] += amt 
            print(f"{amt} has been deposited to {name}'s account.")
        else:
            print(f"Invalid deposit for {name}. Ensure the account exists and the amount is positive.")

    def withdraw(self, name, amt):
        if name in self.accs and 0 < amt <= self.accs[name]:
            self.accs[name] -= amt
            print(f"{amt} has been withdrawn from {name}'s account.")
        else:
            print(f"Invalid withdrawal for {name}. Ensure the account exists and sufficient balance.")

    def get_bal(self, name):
        return self.accs.get(name, None)  

    def display_accs(self):
        if self.accs:
            print("Accounts and their balances:")
            for name, balance in self.accs.items():
                print(f"{name}: {balance}")
        else:
            print("No accounts available.")


def menu():
    bank = Bank()
    
    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Display All Accounts")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            name = input("Enter the name for the new account: ")
            balance = float(input("Enter the initial balance (default is 0): ") or 0)
            bank.create_acc(name, balance)
        
        elif choice == 2:
            name = input("Enter the account name to deposit into: ")
            amt = float(input("Enter the amount to deposit: "))
            bank.deposit(name, amt)
        
        elif choice == 3:
            name = input("Enter the account name to withdraw from: ")
            amt = float(input("Enter the amount to withdraw: "))
            bank.withdraw(name, amt)
        
        elif choice == 4:
            name = input("Enter the account name to check balance: ")
            balance = bank.get_bal(name)
            if balance is None:
                print(f"No account found for {name}.")
            else:
                print(f"{name}'s balance: {balance}")
        
        elif choice == 5:
            bank.display_accs()
        
        elif choice == 6:
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

menu()
