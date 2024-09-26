balance = 0


def print_menu():
    print("Welcome to the ATM ")
    print("What you want to do, Deposit,Withdrawal or Check Balance?")
    print("Type 'D' for deposit, 'W' for withdrawal and 'B' for check balance")


def deposit_cash():
    global balance
    deposit = input("Enter the amount: ")
    if not deposit.isdigit():
        print("The amount should be a digit")
    else:
        deposit = int(deposit)
        balance += deposit
        print(f"You are deposited rs.{deposit} in your account and your current balance is {balance}")


def withdraw_cash():
    global balance
    withdraw = input("Enter the amount: ")
    if not withdraw.isdigit():
        print("The amount should be a digit")
    else:
        withdraw = int(withdraw)
        if withdraw > balance:
            print("Insufficient balance")
        else:
            balance -= withdraw
            print("Withdrawal successfull. your current balance is ", balance)


def check_balance():
    print(f"Your current balance is: {balance}")


while True:
    print_menu()
    user_choice = input("Enter your choice: ").upper()

    if user_choice == 'D':
        deposit_cash()
    elif user_choice == 'W':
        withdraw_cash()
    elif user_choice == 'B':
        check_balance()
    else:
        print("Invalid choice! Please enter 'D', 'W', or 'B'.")

    continue_choice = input("Do you want to perform another operation? (Y/N): ").upper()
    if continue_choice != 'Y':
        print("Thank you for using the ATM. Goodbye!")
        break
