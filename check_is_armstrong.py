def is_armstrong(num):
    num_str = str(num)
    num_count = len(num_str)
    total = 0

    for n in num_str:
        total += int(n) ** num_count

    if total == num:
        return f"The number {num} is an armstrong number"

    else:
        return f"The number {num} is NOT an armstrong number"


user_input = input("Please enter a number: ")
if user_input.isdigit():
    print(is_armstrong(int(user_input)))
else:
    print(f"Error : The input is not an integer")
