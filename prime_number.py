def is_prime(n):
    if n <= 1:
        print("Numbers less than or equal to 1 are not prime.")
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def main():
    try:
        number = int(input("Enter the number:").strip())
        if is_prime(number):
            print(f"The number {number} is a prime number.")

        else:
            print(f"the number {number} is not a prime number")

    except ValueError:
        print("Invalid input. Please enter a valid integer")


main()
