def generate_multiplication_table(number, limit=10):
    if not isinstance(number, int) or number < 0:
        return "Please enter a positive integer "

    table = []
    for i in range(1, limit + 1):
        table.append(f"{i}x{number}= {i * number}")

    return "\n".join(table)


try:
    user_input = int(input("Enter a number to generate its multiplication table: "))
    print(generate_multiplication_table(user_input))

except ValueError:
    print("Invalid input. Please enter a valid integer.")
