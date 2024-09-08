def get_number(num):
    while True:
        try:
            number = float(input(num).strip())
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def find_largest_of_three():
    print("Welcome to the Largest Number Finder!")

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    num3 = get_number("Enter the third number: ")

    largest = max(num1, num2, num3)

    print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")


find_largest_of_three()
