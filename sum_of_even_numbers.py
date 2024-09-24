def valid_input(num):
    while True:
        try:
            user_input = int(input(num))
            if isinstance(user_input, int):
                return user_input
        except ValueError:
            print("Invalid input")


def sum_of_range(star, end):
    total = 0
    for num in range(star, end):
        if num % 2 == 0:
            total += num
    return total


range_start = valid_input("Enter the starting number of the range: ")
range_end = valid_input("enter the ending number of the range: ")
result = sum_of_range(range_start, range_end)
print(f"The sum of even number in the provided range is {result}.")
