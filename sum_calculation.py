def get_number(prompt):
    while True:
        try:
            number = int(input(prompt).strip())
            if number <= 0:
                print("Please enter a positive integer.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def calculate_sum(n):
    return sum(range(1, n + 1))


def main():
    print("Welcome to the Sum Calculator!")
    n = get_number("Enter a positive integer: ")

    result = calculate_sum(n)
    print(f"The sum of all numbers from 1 to {n} is: {result}")


main()
