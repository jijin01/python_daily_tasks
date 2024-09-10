def find_second_largest_num(number):
    unique_number = list(set(number))  # removing duplicates - set do not allow duplicates
    if len(unique_number) < 2:
        return "The list should contain more than two number to find second largest number"
    if not all(isinstance(num, (int, float)) for num in number):
        return "List should contain only numbers."

    unique_number.sort()
    unique_number.reverse()
    return unique_number[1]


number_list = [10, 20, 30, 40, -10, -20, 39.5]
result = find_second_largest_num(number_list)
if isinstance(result, str):  # if there is any string in the provided list it will print the message provided above
    print(result)
else:
    print(f"The second largest number is {result}")