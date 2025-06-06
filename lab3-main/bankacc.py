name = input("Your name - ")
money = int(input("How much money do you initially have? "))

while True:
    print("\nActions:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose an action (1-4): ")

    if choice == '1':
        amount = int(input("Enter amount to deposit: "))
        money += amount
        print("Deposited: $", amount, "On the account: $", money)
    elif choice == '2':
        amount = int(input("Enter amount to withdraw: "))
        if amount <= money:
            money -= amount
            print("Withdrew: $", amount, "On the account: $", money)
        else:
            print("Not enough money on the account")
    elif choice == '3':
        print("On the account: $", money)
    elif choice == '4':
        print("Thank you!")
        break
    else:
        print("Try again.")
