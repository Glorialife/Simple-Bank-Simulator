# 1. Define named constants
MIN_BALANCE = 50.0  # Minimum balance required for transactions 
OVERDRAFT_FEE = 35.0  # A fee applied if an account goes below a minimum balance

# 2. Main function to run the program
def main():
    balance = 100.0  # make sure balance is above min_balance
    
    # Show the menu and ask for user input
    print_menu()
    user_choice = int(input("Enter your choice: "))  # Get the user's choice 1-4

    # Each menu option using if-else
    if user_choice == 1: 
        check_balance(balance) # display the current balance 
    elif user_choice == 2:
        balance = deposit(balance) # to add money to the balance  
    elif user_choice == 3:
        balance = withdraw(balance) # subtract money from the balance (if allowed)
    elif user_choice == 4: 
        exit_program() # to terminate the program with a goodbye message
        return
    else:
        print("Invalid choice, please enter a number between 1 and 4.") # User has to enter 1-4

# 3. Function to display the menu
def print_menu():
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

# 4. Function to check the balance
def check_balance(balance):
    print(f"Your current balance is ${balance}")

# 5. Function to deposit money
def deposit(balance):
    deposit_amount = float(input("Enter the deposit amount: "))
    if deposit_amount > 0:  # Valid deposit
        balance = balance + deposit_amount
        print(f"Deposit successful! Your new balance is ${balance}.")
    else:
        print("Invalid deposit amount. Enter a positive number.")
    return balance

# 6. Function to withdraw money
def withdraw(balance):
    withdraw_amount = float(input("Enter the withdrawal amount: "))
    if withdraw_amount > balance:  # Check if there are enough funds
        print("Withdrawal unsuccessful! Insufficient balance")
    else:
        balance = balance - withdraw_amount  # Subtract the withdrawal amount
        if balance < MIN_BALANCE:  # Check if balance falls below minimum
            print(f"Overdraft! A fee of ${OVERDRAFT_FEE} has been applied.")
            balance = balance - OVERDRAFT_FEE  # Apply overdraft fee
        print(f"Withdrawal successful! Your new balance is ${balance}.")
    return balance

# 7. Function to exit the program
def exit_program():
    print("Thank you for using our banking service! Bye.")

# 8. Call the main function
main()
