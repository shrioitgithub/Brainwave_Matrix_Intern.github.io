class ATM:
    def __init__(self, pin, balance=100000):
        self.pin = pin
        self.balance = balance
        self.islogged_in = False

    def login(self, entered_pin):
        if entered_pin == self.pin:
            self.islogged_in = True
            print("Login successful!")
        else:
            print("Sorry! Incorrect PIN.")

    def balance_check(self):
        if self.islogged_in:
            print(f"Your current balance is: ${self.balance}")
        else:
            print("Please log in first.")

    def deposit(self, amount):
        if self.islogged_in:
            if amount > 0:
                self.balance += amount
                print(f"You've successfully deposited ${amount}. Your current balance is ${self.balance}.")
            else:
                print("Deposit amount must be greater than zero.")
        else:
            print("Please log in first.")

    def withdraw(self, amount):
        if self.islogged_in:
            if amount <= self.balance:
                self.balance -= amount
                print(f"You've successfully withdrawn ${amount}. Your new balance is ${self.balance}.")
            else:
                print("Insufficient Balance.")
        else:
            print("Please log in first.")

    def logout(self):
        self.islogged_in = False
        print("You have logged out successfully.")


def atm():
    print("Welcome to the ATM!")
    pin = "9012"  
    atm = ATM(pin)

    while True:
        print("\nATM Menu:")
        print("1. Log In")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Log Out")
        print("6. Exit")

        choice = input("Please choose an option (1-6): ")

        if choice == "1":
            entered_pin = input("Enter your PIN: ")
            atm.login(entered_pin)
        elif choice == "2":
            atm.balance_check()
        elif choice == "3":
            try:
                amount = float(input("Enter the amount to deposit: $"))
                atm.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "4":
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                atm.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "5":
            atm.logout()
        elif choice == "6":
            print("Thank you for using the ATM. ")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    atm()
