# ATM-like System in Python

def atm():
    global balance  # Declare global to access and modify the balance
    print("Welcome to KCB ATM")
    print("Your balance is $%.2f" % balance)
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
            print("Thank you for using KCB ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def withdraw():
    global balance
    try:
        amount = float(input("How much would you like to withdraw? "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
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
        print("Invalid amount. Please enter a number.")
        return

    if amount <= 0:
        print("Deposit amount must be greater than zero.")
    else:
        balance += amount
        print("Deposit successful. Your new balance is $%.2f" % balance)

def display_balance():
    global balance
    print("Your balance is $%.2f" % balance)

# Initialize balance
balance = 100.00

# Run the ATM system
atm()
