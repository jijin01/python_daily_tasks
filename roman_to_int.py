def roman_to_int(roman):
    total = 0
    prev_value = 0

    for char in reversed(roman):
        if char == 'I':
            value = 1
        elif char == 'V':
            value = 5
        elif char == 'X':
            value = 10
        elif char == 'L':
            value = 50
        elif char == 'C':
            value = 100
        elif char == 'D':
            value = 500
        elif char == 'M':
            value = 1000
        else:
            value = 0

        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total


user_input = input("Enter a Roman numeral: ")
print(f"The integer value is:", roman_to_int(user_input))
