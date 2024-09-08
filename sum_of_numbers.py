def get_number(num):
    while True:
        try:
            number = float(input(num).strip())
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate_sum():
    print("Welcome to the Sum Calculator!")

    num1 = get_number("Please enter the first number: ")

    num2 = get_number("Please enter the second number: ")

    total = num1 + num2
    print(f"The sum of {num1} and {num2} is: {total}")


calculate_sum()
