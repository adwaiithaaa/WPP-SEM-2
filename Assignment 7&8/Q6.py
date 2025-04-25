import random

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  
        self.balance = balance
    
    def deposit(self, amt):
        if amt > 0:
            self.balance += amt
            print(f"{amt} has been deposited into account {self.account_number}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amt):
        if 0 < amt <= self.balance:
            self.balance -= amt
            print(f"{amt} withdrawn from account {self.account_number}.")
        else:
            print(f"Invalid")
    
    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}  
    
    def create_account(self, balance=0):
        account_number = random.randint(1000, 9999)  
        if account_number not in self.accounts:
            new_account = BankAccount(account_number, balance)
            self.accounts[account_number] = new_account
            print(f"Account {account_number} created with balance {balance}.")
            return account_number
        else:
            print(f"Account number {account_number} already exists.")
    
    def get_account(self, account_number):
        return self.accounts.get(account_number, None)
    
    def display_all_accounts(self):
        if self.accounts:
            print("Accounts and their details:")
            for account in self.accounts.values():
                account.display_account_details()
        else:
            print("No accounts available.")
    
def menu():
    bank = Bank()
    
    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account Details")
        print("5. Display All Accounts")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            balance = float(input("Enter the initial balance: ") or 0)
            account_number = bank.create_account(balance)
        
        elif choice == 2:
            account_number = int(input("Enter the account number to deposit into: "))
            amt = float(input("Enter deposit amount: "))
            account = bank.get_account(account_number)
            if account:
                account.deposit(amt)
            else:
                print(f"Account {account_number} not found.")
        
        elif choice == 3:
            account_number = int(input("Enter the account number to withdraw from: "))
            amt = float(input("Enter the amount to withdraw: "))
            account = bank.get_account(account_number)
            if account:
                account.withdraw(amt)
            else:
                print(f"Account {account_number} not found.")
        
        elif choice == 4:
            account_number = int(input("Enter the account number to display details: "))
            account = bank.get_account(account_number)
            if account:
                account.display_account_details()
            else:
                print(f"Account {account_number} not found.")
        
        elif choice == 5:
            bank.display_all_accounts()
        
        elif choice == 6:
            break
        
        else:
            print("Invalid choice.")

menu()
