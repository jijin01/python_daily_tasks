def get_number_of_terms(num):
    while True:
        try:
            terms = int(input(num).strip())
            if terms <= 0:
                print("Please enter a positive integer.")
            else:
                return terms
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def print_fibonacci_sequence(n):
    a, b = 0, 1
    sequence = []

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def main():
    print("Welcome to the Fibonacci Sequence Generator!")

    num_terms = get_number_of_terms("Enter the number of terms you want in the Fibonacci sequence: ")

    fibonacci_sequence = print_fibonacci_sequence(num_terms)
    print(f"Fibonacci sequence with {num_terms} terms: {fibonacci_sequence}")


main()
