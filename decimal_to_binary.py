def valid_input(num):
    while True:
        user_input = input(num)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input")


def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return '0'

    binary = ''

    while decimal_num > 0:
        remainder = decimal_num % 2
        binary = str(remainder) + binary
        decimal_num = decimal_num // 2

    return binary


decimal_number = valid_input("Enter a decimal number: ")
binary_number = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is: {binary_number}")
