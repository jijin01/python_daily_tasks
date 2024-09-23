def greatest_cmn_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def find_lcm(a, b):
    return abs(a * b) // greatest_cmn_divisor(a, b)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = find_lcm(num1, num2)
print(f" The LCM of the numbers you have entered is {result}.")
