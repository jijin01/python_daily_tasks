def get_number(integer):
    while True:
        try:
            number = int(input(integer).strip())
            if number < 0:
                print("Factorial is not defined for negative numbers. Please enter a non-negative integer.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def calculate_factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def main():
    print("Welcome to the Factorial Calculator!")
    number = get_number("Please enter a non-negative integer: ")

    result = calculate_factorial(number)
    print(f"The factorial of {number} is: {result}")


main()
