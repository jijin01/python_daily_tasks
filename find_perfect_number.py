def find_perfect_num(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    if total == n:
        return f"The number {n} is a perfect number"
    else:
        return f"The number {n} is Not a perfect number"


def valid_input(digit):
    while True:
        number = input(digit)
        if number.isdigit():
            return int(number)
        else:
            print("Invalid input")


num = valid_input(" Enter a number: ")
result = find_perfect_num(num)
print(result)
