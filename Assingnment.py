# ATM-like System in Python

def atm():
    # Ask for user name and initial balance during account creation
    name = input("Please enter your name: ")
    global balance
    while True:
        try:
            balance = float(input("Please enter your initial balance: "))
            if balance < 0:
                print("Initial balance cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    print(f"\nAccount created successfully for {name} with a balance of $%.2f!\n" % balance)

    print(f"Welcome to KCB ATM, {name}!")
    print("What would you like to do today?")

    while True:
        print("\nEnter 1 to withdraw")
        print("Enter 2 to deposit")
        print("Enter 3 to display balance")
        print("Enter 4 to exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            withdraw()
        elif choice == 2:
            deposit()
        elif choice == 3:
            display_balance()
        elif choice == 4:
            print(f"Thank you for using KCB ATM, {name}. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def withdraw():
    global balance
    try:
        amount = float(input("How much would you like to withdraw? "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    if amount > balance:
        print("You cannot withdraw more than your balance.")
    elif amount <= 0:
        print("Withdrawal amount must be greater than zero.")
    else:
        balance -= amount
        print("Withdrawal successful. Your new balance is $%.2f" % balance)

def deposit():
    global balance
    try:
        amount = float(input("How much would you like to deposit? "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    if amount <= 0:
        print("Deposit amount must be greater than zero.")
    else:
        balance += amount
        print("Deposit successful. Your new balance is $%.2f" % balance)

def display_balance():
    global balance
    print("Your current balance is $%.2f" % balance)

# Initialize balance
balance = 0.00

# Run the ATM system
atm()
