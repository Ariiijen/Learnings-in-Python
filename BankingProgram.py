class BankAccount:
    def __init__(self, account_name, balance=0):
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("\n Invalid deposit amount. Please enter a positive number.")
            return
        self.balance += amount
        print(f"\n Successfully deposited {amount}. Your new balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= 0:
            print("\n Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print("\n Insufficient balance! Transaction denied.")
            return
        self.balance -= amount
        print(f"\n Successfully withdrew {amount}. Your remaining balance is {self.balance}.")

    def check_balance(self):
        print(f"\n Current Balance: {self.balance}")

    def account_details(self):
        print("\n ACCOUNT DETAILS")
        print("-" * 30)
        print(f" Account Holder : {self.account_name}")
        print(f" Current Balance: {self.balance}")
        print("-" * 30)


# Initialize Account
account = BankAccount("Allyza Jane Espragera")

# Banking Menu Loop
while True:
    print("\n" + "=" * 40)
    print(" BANKING PROGRAM - DATA STRUCTURES & ALGORITHM")
    print(" February 11, 2025 - IT1R5")
    print("=" * 40)
    print("1.  Check Balance")
    print("2.  Deposit Funds")
    print("3.  Withdraw Funds")
    print("4.  View Account Details")
    print("=" * 40)

    choice = input(" Enter your choice: ")

    if choice == '1':
        account.check_balance()
    elif choice == '2':
        try:
            amount = float(input(" Enter deposit amount: "))
            account.deposit(amount)
        except ValueError:
            print("\n Invalid input! Please enter a numeric value.")
    elif choice == '3':
        try:
            amount = float(input(" Enter withdrawal amount: "))
            account.withdraw(amount)
        except ValueError:
            print("\n Invalid input! Please enter a numeric value.")
    elif choice == '4':
        account.account_details()
    elif choice == '5':
        print("\n Thank you for using our banking system! Have a great day. ^^")
        break
    else:
        print("\n Invalid choice. Please select a valid option.")