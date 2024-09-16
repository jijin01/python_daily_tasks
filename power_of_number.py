def valid_input(num):
    while True:
        try:
            value = int(input(num))
            return value

        except ValueError:
            print("The input should be an integer")


def power_calculation(base, exponent):
    result = 1
    for _ in range(exponent):
        result = result * base
    return result


base = valid_input("Enter the base: ")
exponent = valid_input("enter the exponent: ")
print(f"{base} raised to the power of {exponent} is: {power_calculation(base, exponent)}")
