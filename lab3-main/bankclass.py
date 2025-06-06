class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}. Current balance: ${self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")
        else:
            print("Not enough on the account")

def main():
    name = input("Your name - ")
    money = int(input("How much money do you initially have? "))
    account = BankAccount(name, money)

    while True:
        print("\nActions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an action (1-4): ")

        if choice == '1':
            amount = int(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = int(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            print(f"Current balance: ${account.balance}")
        elif choice == '4':
            print("Thank you")
            break
        else:
            print("Try again")

if __name__ == "__main__":
    main()
