def get_integer(digit):
    while True:
        try:
            number = int(input(digit).strip())
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def check_even_or_odd():
    print("Welcome to the Even or Odd Checker!")

    number = get_integer("Please enter an integer: ")

    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")


check_even_or_odd()
