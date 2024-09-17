def calculate_average(numbers):
    valid_numbers = [num for num in numbers if isinstance(num, (int, float))]

    if len(valid_numbers) == 0:
        return "No valid numbers to calculate the average."

    total = sum(valid_numbers)
    count = len(valid_numbers)
    average = total / count
    return round(average, 2)


list1 = [24, "apple", 30, 45, 70.5, 90, "banana", 98, 85, 43]


print(calculate_average(list1))
